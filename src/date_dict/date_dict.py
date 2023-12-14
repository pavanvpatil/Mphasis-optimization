from datetime import datetime
from src import inventory_dict


def get_date_inventory_list_dict() -> dict[datetime, list[str]]:
    '''This function returns a dictionary of dates and inventory ids

    :param None
    :return: dictionary of dates and inventory ids
    :rtype: dict[datetime, list[str]]
    '''

    date_inventory_list_dict: dict[datetime, list[str]] = {}
    sorted_inventory_list = sorted(inventory_dict.values(), key=lambda x: datetime.strptime(
        x.departuredatetime, "%d-%m-%Y %H:%M"))

    for inventory_obj in sorted_inventory_list:
        if datetime.strptime(inventory_obj.departuredate, "%m-%d-%Y") in date_inventory_list_dict:
            date_inventory_list_dict[datetime.strptime(
                inventory_obj.departuredate, "%m-%d-%Y")].append(inventory_obj.inventoryid)
        else:
            date_inventory_list_dict[datetime.strptime(
                inventory_obj.departuredate, "%m-%d-%Y")] = [inventory_obj.inventoryid]

    return date_inventory_list_dict


date_inventory_list_dict = get_date_inventory_list_dict()
