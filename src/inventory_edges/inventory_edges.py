from src import date_inventory_list_dict
from src import inventory_dict, schedule_dict
from datetime import datetime, timedelta, time


def get_inventory_edges(inventory_id_affected: str) -> list[str]:
    '''This function returns a list of inventory ids that are valid for the given affected inventory id

    :param inventory_id_affected: inventory id of the affected inventory
    :type inventory_id_affected: str
    :return: list of inventory ids that are valid for the given affected inventory id
    :rtype: list[str]
    '''

    departure_date = datetime.strptime(
        inventory_dict[inventory_id_affected].departuredate, '%m-%d-%Y')
    departure_time = datetime.strptime(
        schedule_dict[inventory_dict[inventory_id_affected].scheduleid].departuretime, '%H:%M').time()

    list_of_valid_dates = [departure_date +
                           timedelta(days=i) for i in range(0, 4)]

    list_of_valid_inventory_ids = []

    for inventory_id in date_inventory_list_dict[list_of_valid_dates[0]]:
        if inventory_dict[inventory_id].is_affected == True:
            continue
        curr_inventory_departure_time = datetime.strptime(
            schedule_dict[inventory_dict[inventory_id].scheduleid].departuretime, '%H:%M').time()
        if curr_inventory_departure_time >= departure_time and inventory_id != inventory_id_affected:
            list_of_valid_inventory_ids.append(inventory_id)

    for inventory_id in date_inventory_list_dict[list_of_valid_dates[1]]:
        if inventory_dict[inventory_id].is_affected == True:
            continue
        list_of_valid_inventory_ids.append(inventory_id)

    for inventory_id in date_inventory_list_dict[list_of_valid_dates[2]]:
        if inventory_dict[inventory_id].is_affected == True:
            continue
        list_of_valid_inventory_ids.append(inventory_id)

    for inventory_id in date_inventory_list_dict[list_of_valid_dates[3]]:
        if inventory_dict[inventory_id].is_affected == True:
            continue
        curr_inventory_departure_time = datetime.strptime(
            schedule_dict[inventory_dict[inventory_id].scheduleid].departuretime, '%H:%M').time()
        if curr_inventory_departure_time <= departure_time:
            list_of_valid_inventory_ids.append(inventory_id)
        else:
            break

    return list_of_valid_inventory_ids
