from src.flight_geo import get_distance_from_airport_codes
from src import inventory_dict
from src.gui.gui import flight_ranking_values_obj
from datetime import datetime


def get_distance_score(
    destination_airport_code: str,
    final_airport_code: str,
) -> float:
    '''Function to calculate the distance score
    score = DIST_SCORE / (1 + (distance / 100)^2)

    :param destination_airport_code: destination airport code
    :type destination_airport_code: str
    :param final_airport_code: final airport code
    :type final_airport_code: str
    :return: distance score 
    :rtype: float
    '''

    distance = get_distance_from_airport_codes(
        airport_code1=destination_airport_code,
        airport_code2=final_airport_code
    )
    return float(flight_ranking_values_obj.distance_score/(((distance / 100.0) ** 2) + 1))


def get_arrival_time_score(
    inventory_id_affected: str,
    inventory_id_proposed_arrival: str,
) -> float:
    '''Function to calculate the arrival time score
    score = ARR_SCORE / (1 + (arrival time difference / 10)^2)

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param inventory_id_proposed_arrival: inventory id of the proposed arrival flight
    :type inventory_id_proposed_arrival: str
    :return: arrival time score
    :rtype: float
    '''

    affected_inventory = inventory_dict[inventory_id_affected]
    proposed_departure_inventory = inventory_dict[inventory_id_proposed_arrival]

    dt_affected_arrival_date_time = datetime.strptime(
        affected_inventory.arrivaldatetime, '%d-%m-%Y %H:%M')

    dt_proposed_arrival_date_time = datetime.strptime(
        proposed_departure_inventory.arrivaldatetime, '%d-%m-%Y %H:%M')

    arrival_time_difference: float = abs(
        (dt_affected_arrival_date_time - dt_proposed_arrival_date_time).total_seconds())

    return float(flight_ranking_values_obj.arr_time_multiplier/(((arrival_time_difference / 36000) ** 2) + 1))


def get_departure_time_score(
    inventory_id_affected: str,
    inventory_id_proposed_departure: str,
) -> float:
    '''Function to calculate the departure time score
    score = DEP_SCORE / (1 + (departure time difference / 10)^2)

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param inventory_id_proposed_departure: inventory id of the proposed departure flight
    :type inventory_id_proposed_departure: str
    :return: departure time score
    :rtype: float
    '''

    affected_inventory = inventory_dict[inventory_id_affected]
    proposed_departure_inventory = inventory_dict[inventory_id_proposed_departure]

    dt_affected_departure_date_time = datetime.strptime(
        affected_inventory.departuredatetime, '%d-%m-%Y %H:%M')

    dt_proposed_departure_date_time = datetime.strptime(
        proposed_departure_inventory.departuredatetime, '%d-%m-%Y %H:%M')

    departure_time_difference: float = abs(
        (dt_affected_departure_date_time - dt_proposed_departure_date_time).total_seconds())

    return float(flight_ranking_values_obj.arr_time_multiplier/(((departure_time_difference / 36000) ** 2) + 1))


def get_equipment_score(inventory_id_affected: str, path_inventory_ids: list[str]) -> float:
    '''Function to calculate the equipment score
    score = (x/n) * EQUIP_SCORE
    where x is the number of flights with the same equipment as the affected flight
    and n is the total number of flights in the proposed sequence

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param path_inventory_ids: list of inventory ids of the flights in the proposed sequence
    :type path_inventory_ids: list[str]

    :return: equipment score
    :rtype: float
    '''

    aircraft_type_affected = inventory_dict[inventory_id_affected].aircrafttype

    count_of_same_aircraft_type = 0

    for inventory_id in path_inventory_ids:
        if inventory_dict[inventory_id].aircrafttype == aircraft_type_affected:
            count_of_same_aircraft_type += 1

    return float((count_of_same_aircraft_type/len(path_inventory_ids)) * flight_ranking_values_obj.equipment_multiplier)


def get_stop_over_score(
    path_inventory_ids_len: int
) -> float:
    '''Function to calculate the stop over score
    score = -20 if the proposed sequence has more than one flight

    :param path_inventory_ids_len: length of the proposed sequence
    :type path_inventory_ids_len: int
    :return: stop over score
    :rtype: float
    '''

    return flight_ranking_values_obj.stop_over_score if path_inventory_ids_len > 1 else 0.0


def get_alternate_flight_path_score(
    inventory_id_affected: str,
    path_inventory_ids: list[str],
) -> float:
    '''Function to calculate the alternate flight path score
    score = distance score + arrival time score + departure time score + equipment score + stop over score

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param path_inventory_ids: list of inventory ids of the flights in the proposed sequence
    :type path_inventory_ids: list[str]
    :return: flight path score
    :rtype: float
    '''
    destination_airport_code = inventory_dict[inventory_id_affected].arrivalairport
    final_airport_code = inventory_dict[path_inventory_ids[-1]].arrivalairport

    return get_distance_score(destination_airport_code=destination_airport_code, final_airport_code=final_airport_code) + \
        get_arrival_time_score(inventory_id_affected=inventory_id_affected, inventory_id_proposed_arrival=path_inventory_ids[-1]) + \
        get_departure_time_score(inventory_id_affected=inventory_id_affected, inventory_id_proposed_departure=path_inventory_ids[0]) + \
        get_equipment_score(inventory_id_affected=inventory_id_affected,
                            path_inventory_ids=path_inventory_ids) + \
        get_stop_over_score(path_inventory_ids_len=len(path_inventory_ids))


def get_top_alternate_paths(
    inventory_id_affected: str,
    all_paths: list[list[str]],
    no_of_top_alternate_paths: int,
) -> list[tuple[list[str], float]]:
    '''Function to get the top 5 alternate paths based on the flight path score

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param all_paths: list of all paths from source airport to destination airport
    :type all_paths: list[list[str]]
    :param no_of_top_alternate_paths: number of top alternate paths to be returned
    :type no_of_top_alternate_paths: int
    :return: list of top alternate paths
    :rtype: list[tuple[list[str], float]]
    '''

    alternate_paths = []
    for path in all_paths:
        alternate_paths.append(
            (path, get_alternate_flight_path_score(inventory_id_affected=inventory_id_affected, path_inventory_ids=path)))

    alternate_paths.sort(key=lambda x: x[1], reverse=True)

    return alternate_paths[:no_of_top_alternate_paths]
