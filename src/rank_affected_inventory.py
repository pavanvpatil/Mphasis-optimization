from src.rank_pnrs import get_avg_pnr_score


def rank_affected_inventories(
    affected_inventory_ids: list[str],
) -> list[str]:
    '''Returns a list of inventories sorted in descending order of average pnr score

    AVG_PNR_SCORE = SUM(PNR_SCORE)/NUM_PNRS

    :param affected_inventory_ids: list of inventory IDs of affected flights
    :param type: list[str]
    :return: list of inventories sorted in descending order of average pnr score
    :rtype: list[str]
    '''

    inventory_id_score_dict = {}

    for inventory_id in affected_inventory_ids:
        inventory_id_score_dict[inventory_id] = get_avg_pnr_score(inventory_id)

    return sorted(inventory_id_score_dict, key=inventory_id_score_dict.get, reverse=True)
