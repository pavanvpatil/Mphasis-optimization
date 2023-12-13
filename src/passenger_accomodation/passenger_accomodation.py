from src.rank_pnrs import get_ranked_affected_passenger_doc_ids
from src import inventory_dict, passenger_dict, booking_dict
from src.classes.flight.inventory import Inventory
from src.classes.pnr.passenger import Passenger
import copy


def can_accomodate_passenger_in_an_inventory(
    inventory_obj: Inventory,
    cabin_code: str,
) -> bool:
    can_accomodate = False
    if cabin_code == 'FirstClass':
        inventories_left = inventory_obj.fc_availableinventory - \
            inventory_obj.fc_bookedinventory
        if inventories_left > 0:
            can_accomodate = True
    elif cabin_code == 'BusinessClass':
        inventories_left = inventory_obj.bc_availableinventory - \
            inventory_obj.bc_bookedinventory
        if inventories_left > 0:
            can_accomodate = True
    elif cabin_code == 'PremiumEconomyClass':
        inventories_left = inventory_obj.pc_availableinventory - \
            inventory_obj.pc_bookedinventory
        if inventories_left > 0:
            can_accomodate = True
    elif cabin_code == 'EconomyClass':
        inventories_left = inventory_obj.ec_availableinventory - \
            inventory_obj.ec_bookedinventory
        if inventories_left > 0:
            can_accomodate = True
    return can_accomodate


def accomodate_passengers_path(
    affected_ordered_passenger_booking_ids: list[str],
    ranked_affected_passengers: list[str],
    path: list[str],
) -> tuple[list[str], list[Inventory]]:
    '''
    This function accomodates passengers in the given path
    param ranked_affected_passengers: list of doc_ids of affected passengers
    type ranked_affected_passengers: list[str]
    param path: list of inventory ids of the path
    type path: list[str]
    return: number of passengers accomodated
    rtype: int
    '''

    inventory_objs = [copy.deepcopy(inventory_dict[inventory_id])
                      for inventory_id in path]

    accomodated_passenger_doc_ids = []

    for index in range(len(ranked_affected_passengers)):

        cabin_code = booking_dict[affected_ordered_passenger_booking_ids[index]].cos_cd

        is_overall_accomodated = True

        for inventory_obj in inventory_objs:
            is_overall_accomodated = is_overall_accomodated and can_accomodate_passenger_in_an_inventory(
                inventory_obj=inventory_obj,
                cabin_code=cabin_code
            )

        if is_overall_accomodated == True:
            for inventory_obj in inventory_objs:
                if cabin_code == 'FirstClass':
                    inventory_obj.fc_bookedinventory += 1
                elif cabin_code == 'BusinessClass':
                    inventory_obj.bc_bookedinventory += 1
                elif cabin_code == 'PremiumEconomyClass':
                    inventory_obj.pc_bookedinventory += 1
                elif cabin_code == 'EconomyClass':
                    inventory_obj.ec_bookedinventory += 1
            accomodated_passenger_doc_ids.append(
                ranked_affected_passengers[index]
            )

    return (accomodated_passenger_doc_ids, inventory_objs)


def accomodate_passengers(
    affected_inventory_id: str,
    top_alternate_paths: list[tuple[list[str], float]],
):

    ranked_affected_passengers = get_ranked_affected_passenger_doc_ids(
        inventory_id=affected_inventory_id)

    affected_ordered_passenger_booking_ids = []

    affected_flight_number = inventory_dict[affected_inventory_id].flightnumber
    affected_carrier_code = inventory_dict[affected_inventory_id].carriercode

    for passenger_doc_id in ranked_affected_passengers:
        affected_ordered_passenger_booking_ids.append(
            str(passenger_dict[passenger_doc_id].recloc) + ":" +
            str(affected_carrier_code) + ":" + str(affected_flight_number)
        )

    output = []
    for path in top_alternate_paths:
        output.append(accomodate_passengers_path(
            ranked_affected_passengers=ranked_affected_passengers,
            affected_ordered_passenger_booking_ids=affected_ordered_passenger_booking_ids,
            path=path[0]
        ))

    output.sort(key=lambda x: len(x[0]), reverse=True)

    return output[0]
