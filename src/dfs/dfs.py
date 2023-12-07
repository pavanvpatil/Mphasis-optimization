from src import inventory_dict
from src.dfs.create_graph import get_adjacency_list


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

    if current_airport_code == destination_airport_code:
        all_paths.append(cur_path.copy())
        return

    if depth > 4:
        return

    visited_airport_codes.add(current_airport_code)

    for inventory_id in adjacency_list[current_airport_code]:

        cur_path.append(inventory_id)

        inventory = inventory_dict[inventory_id]
        next_airport_code = inventory.arrivalairport

        if next_airport_code not in visited_airport_codes:
            dfs(
                adjacendy_list=adjacency_list,
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
) -> None:
    '''Setup required inputs for dfs and call dfs function

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :return: None
    :rtype: None
    '''

    adjacency_list = get_adjacency_list(
        inventory_id_affected=inventory_id_affected
    )

    inventory = inventory_dict[inventory_id_affected]
    source_airport_code = inventory.departureairport
    destination_airport_code = inventory.arrivalairport

    visited_airport_codes = set()
    cur_path = []
    all_paths = []

    dfs(
        adjacency_list=adjacency_list,
        visited_airport_codes=visited_airport_codes,
        cur_path=cur_path,
        all_paths=all_paths,
        current_airport_code=source_airport_code,
        destination_airport_code=destination_airport_code,
        depth=0
    )
