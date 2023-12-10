from src import inventory_dict
from src.flight_geo import get_distance_from_airport_codes


def select_min_source(adjacency_list: dict[str, list[str]], inventory_id_affected: str) -> str:
    '''Select the source airport code for the affected flight based on the distance
    from the source airport code to the other airport codes in the graph

    :param adjacency_list: adjacency list of the graph
    :type adjacency_list: dict[str, list[str]]
    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :return: the source airport code for the affected flight
    :rtype: str
    '''

    affected_src_airport_code = inventory_dict[inventory_id_affected].departureairport

    if len(adjacency_list[affected_src_airport_code]) == 0:
        return affected_src_airport_code

    airport_codes_list: list[str] = list(adjacency_list.keys())

    min_distance = float('inf')
    min_distance_source_airport_code = ""

    for airport_code in airport_codes_list:
        if airport_code == affected_src_airport_code:
            continue

        distance = get_distance_from_airport_codes(
            airport_code1=affected_src_airport_code,
            airport_code2=airport_code
        )

        if distance < min_distance:
            min_distance = distance
            min_distance_source_airport_code = airport_code

    return min_distance_source_airport_code
