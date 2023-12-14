from src.rank_pnrs import get_ranked_affected_passenger_doc_ids
from src import inventory_dict, passenger_dict, booking_dict
from src.classes.flight.inventory import Inventory
from src.classes.pnr.passenger import Passenger
import copy


def can_accomodate_passenger_in_an_inventory(
    inventory_obj: Inventory,
    cabin_code: str,
) -> bool:
    '''Accomodate passenger in an inventory

    :param inventory_obj: inventory object
    :type inventory_obj: Inventory
    :param cabin_code: cabin code
    :type cabin_code: str
    :return: True if passenger can be accomodated in the inventory
    :rtype: bool
    '''
    can_accomodate = False
    if cabin_code == 'FirstClass' and inventory_obj.fc_availableinventory > 0:
        can_accomodate = True
    elif cabin_code == 'BusinessClass' and inventory_obj.bc_availableinventory > 0:
        can_accomodate = True
    elif cabin_code == 'PremiumEconomyClass' and inventory_obj.pc_availableinventory > 0:
        can_accomodate = True
    elif cabin_code == 'EconomyClass' and inventory_obj.ec_availableinventory > 0:
        can_accomodate = True
    return can_accomodate


def update_inventory_obj(inventory_obj: Inventory, cabin_code: str) -> None:
    '''Update inventory accomodation info based on cabin code

    :param inventory_obj: inventory object
    :type inventory_obj: Inventory
    :param cabin_code: cabin code
    :type cabin_code: str
    :return: None
    :rtype: None
    '''
    if cabin_code == 'FirstClass':
        inventory_obj.fc_bookedinventory += 1
        inventory_obj.fc_availableinventory -= 1
        inventory_obj.fc_oversold = inventory_obj.firstclass - \
            inventory_obj.fc_bookedinventory
    elif cabin_code == 'BusinessClass':
        inventory_obj.bc_bookedinventory += 1
        inventory_obj.bc_availableinventory -= 1
        inventory_obj.bc_oversold = inventory_obj.businessclass - \
            inventory_obj.bc_bookedinventory
    elif cabin_code == 'PremiumEconomyClass':
        inventory_obj.pc_bookedinventory += 1
        inventory_obj.pc_availableinventory -= 1
        inventory_obj.pc_oversold = inventory_obj.premiumeconomyclass - \
            inventory_obj.pc_bookedinventory
    elif cabin_code == 'EconomyClass':
        inventory_obj.ec_bookedinventory += 1
        inventory_obj.ec_availableinventory -= 1
        inventory_obj.ec_oversold = inventory_obj.economyclass - \
            inventory_obj.ec_bookedinventory

    inventory_obj.bookedinventory += 1
    inventory_obj.availableinventory -= 1
    inventory_obj.oversold = inventory_obj.bookedinventory - inventory_obj.totalcapacity


def accomodate_passengers_path(
    affected_ordered_passenger_booking_ids: list[str],
    ranked_affected_passengers_doc_ids: list[str],
    path: list[str],
) -> tuple[list[str], list[Inventory]]:
    '''
    This function accomodates passengers in the given path
    param ranked_affected_passengers: list of doc_ids of affected passengers
    type ranked_affected_passengers: list[str]
    param path: list of inventory ids of the path
    type path: list[str]
    return: list of doc_ids of accomodated passengers, list of inventory objects for a path
    rtype: tuple[list[str], list[Inventory]]
    '''

    inventory_objs = [copy.deepcopy(inventory_dict[inventory_id])
                      for inventory_id in path]

    accomodated_passenger_doc_ids = []

    for index in range(len(ranked_affected_passengers_doc_ids)):

        cabin_code = booking_dict[affected_ordered_passenger_booking_ids[index]].cos_cd

        is_overall_accomodated = True

        for inventory_obj in inventory_objs:
            is_overall_accomodated = is_overall_accomodated and can_accomodate_passenger_in_an_inventory(
                inventory_obj=inventory_obj,
                cabin_code=cabin_code
            )

        if is_overall_accomodated == True:
            accomodated_passenger_doc_ids.append(
                ranked_affected_passengers_doc_ids[index])
            for inventory_obj in inventory_objs:
                update_inventory_obj(
                    inventory_obj=inventory_obj,
                    cabin_code=cabin_code
                )

    return (accomodated_passenger_doc_ids, inventory_objs)


def accomodate_passengers(
    affected_inventory_id: str,
    ranked_affected_passengers_doc_ids: list[str],
    top_alternate_paths: list[tuple[list[str], float]],
) -> list[tuple[list[str], list[Inventory]]]:
    '''Accomodate passengers in the top alternate paths for the affected inventory

    :param affected_inventory_id: inventory id of the affected inventory
    :type affected_inventory_id: str
    :param ranked_affected_passengers_doc_ids: list of doc_ids of affected passengers sorted by priority
    :type ranked_affected_passengers_doc_ids: list[str]
    :param top_alternate_paths: list of top alternate paths
    :type top_alternate_paths: list[tuple[list[str], float]]
    :return: list of top accomodations
    :rtype: list[tuple[list[str], list[Inventory]]]
    '''

    affected_ordered_passenger_booking_ids = []

    affected_flight_number = inventory_dict[affected_inventory_id].flightnumber
    affected_carrier_code = inventory_dict[affected_inventory_id].carriercode

    for passenger_doc_id in ranked_affected_passengers_doc_ids:
        affected_ordered_passenger_booking_ids.append(
            str(passenger_dict[passenger_doc_id].recloc) + ":" +
            str(affected_carrier_code) + ":" + str(affected_flight_number)
        )

    top_accomodations = []

    for path in top_alternate_paths:
        top_accomodations.append(accomodate_passengers_path(
            ranked_affected_passengers_doc_ids=ranked_affected_passengers_doc_ids,
            affected_ordered_passenger_booking_ids=affected_ordered_passenger_booking_ids,
            path=path[0]
        ))

    top_accomodations.sort(key=lambda x: len(x[0]), reverse=True)

    for inventory_obj_output in top_accomodations[0][1]:
        inventory_id = inventory_obj_output.inventoryid
        old_inventory_obj = inventory_dict[inventory_id]
        inventory_dict[inventory_id] = copy.deepcopy(
            inventory_obj_output)
        del old_inventory_obj  # dictionary old inventory object is deleted
        del inventory_obj_output  # copied inventory object is deleted
        inventory_obj_output = inventory_dict[inventory_id]

    return top_accomodations
