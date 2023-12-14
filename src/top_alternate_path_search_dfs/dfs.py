from src import inventory_dict
from src.top_alternate_path_search_dfs.create_graph import get_adjacency_list
from src.top_alternate_path_search_dfs.flight_path_score.score import get_top_alternate_paths
from src.inventory_edges.inventory_edges import get_inventory_edges
from src.top_alternate_path_search_dfs.select_source import select_min_source
from datetime import datetime


def check_time_constraint(inventory_id_prev: str, inventory_id_next: str) -> bool:
    '''Check if the time constraint is satisfied between two flights

    :param inventory_id_prev: inventory id of the previous flight
    :type inventory_id_prev: str
    :param inventory_id_next: inventory id of the next flight
    :type inventory_id_next: str
    :return: True if time constraint is satisfied, False otherwise
    :rtype: bool
    '''

    inventory_prev = inventory_dict[inventory_id_prev]
    inventory_next = inventory_dict[inventory_id_next]

    dt_arrival_date_time = datetime.strptime(
        inventory_prev.arrivaldatetime, '%d-%m-%Y %H:%M')

    dt_departure_date_time = datetime.strptime(
        inventory_next.departuredatetime, '%d-%m-%Y %H:%M')

    return (dt_departure_date_time - dt_arrival_date_time).total_seconds() >= 3600 and (dt_departure_date_time - dt_arrival_date_time).total_seconds() <= 43200


def dfs(
    adjacency_list: dict[str, list[str]],
    visited_airport_codes: set[str],
    cur_path: list[str],
    all_paths: list[list[str]],
    current_airport_code: str,
    destination_airport_code: str,
    depth: int,
) -> None:
    '''Depth first search to find all paths from source airport to destination airport

    :param adjacendy_list: adjacency list of the graph
    :type adjacendy_list: dict[str, list[str]]
    :param visited_airport_codes: set of visited_airport_codes airport codes
    :type visited_airport_codes: set[str]
    :param cur_path: current path consisting of inventory ids
    :type cur_path: list[str]
    :param all_paths: list of all paths from source airport to destination airport
    :type all_paths: list[list[str]]
    :param current_airport_code: current airport code
    :type current_airport_code: str
    :param destination_airport_code: destination airport code
    :type destination_airport_code: str
    :param depth: depth of the current node in the graph
    :type depth: int
    :return: None
    :rtype: None
    '''

    if len(cur_path) > 0 and (current_airport_code == destination_airport_code or depth == 4):
        all_paths.append(cur_path.copy())
        return

    if len(cur_path) > 0 and (current_airport_code not in adjacency_list):
        all_paths.append(cur_path.copy())
        return

    visited_airport_codes.add(current_airport_code)

    if len(cur_path) > 0:
        all_paths.append(cur_path.copy())

    for inventory_id in adjacency_list[current_airport_code]:

        inventory = inventory_dict[inventory_id]
        next_airport_code = inventory.arrivalairport

        if next_airport_code not in visited_airport_codes:

            if len(cur_path) > 0 and (not check_time_constraint(cur_path[-1], inventory_id)):
                continue

            cur_path.append(inventory_id)

            dfs(
                adjacency_list=adjacency_list,
                visited_airport_codes=visited_airport_codes,
                cur_path=cur_path,
                all_paths=all_paths,
                current_airport_code=next_airport_code,
                destination_airport_code=destination_airport_code,
                depth=depth+1
            )

            cur_path.pop()

    visited_airport_codes.remove(current_airport_code)


def init_dfs(
    inventory_id_affected: str,
) -> list[tuple[list[str], float]]:
    '''Setup required inputs for dfs and call dfs function and return top alternate paths

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :return: list of top alternate paths
    :rtype: list[tuple[list[str], float]]
    '''

    inventory_id_list = get_inventory_edges(
        inventory_id_affected=inventory_id_affected)

    adjacency_list = get_adjacency_list(
        inventory_id_affected=inventory_id_affected,
        inventory_id_list=inventory_id_list
    )

    affected_inventory = inventory_dict[inventory_id_affected]
    source_airport_code = select_min_source(adjacency_list=adjacency_list,
                                            inventory_id_affected=inventory_id_affected)
    destination_airport_code = affected_inventory.arrivalairport

    visited_airport_codes: set[str] = set()
    cur_path: list[str] = []
    all_paths: list[list[str]] = []

    dfs(
        adjacency_list=adjacency_list,
        visited_airport_codes=visited_airport_codes,
        cur_path=cur_path,
        all_paths=all_paths,
        current_airport_code=source_airport_code,
        destination_airport_code=destination_airport_code,
        depth=0
    )

    return get_top_alternate_paths(
        inventory_id_affected=inventory_id_affected,
        all_paths=all_paths,
        no_of_top_alternate_paths=3)
