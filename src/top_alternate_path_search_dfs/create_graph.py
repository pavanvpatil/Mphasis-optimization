from src import inventory_dict


def get_adjacency_list(
    inventory_id_affected: str,
    inventory_id_list: list[str],
) -> dict[str, list[str]]:
    '''Create graph edges as flights between airports. The graph is 
    represented as an adjacency list. Returns the adjacency list

    :param inventory_id_affected: inventory id of the affected flight
    :type inventory_id_affected: str
    :param inventory_id_list: list of inventory ids of the flights that are to be
    considered for rebooking
    :type inventory_id_list: list[str]
    :return: adjacency list of the graph
    :rtype: dict[str, list[str]]
    '''
    affected_inventory = inventory_dict[inventory_id_affected]
    source_airport_code = affected_inventory.departureairport
    destination_airport_code = affected_inventory.arrivalairport

    # key: airport code A , value: list of inventory ids that depart from airport code A
    adjacency_list: dict[str, list[str]] = dict()
    adjacency_list[source_airport_code] = []
    adjacency_list[destination_airport_code] = []

    for inventory_id in inventory_id_list:
        inventory = inventory_dict[inventory_id]
        adjacency_list[inventory.departureairport].append(inventory_id)

    return adjacency_list
