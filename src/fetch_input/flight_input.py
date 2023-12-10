import os
from pandas import read_csv
from dotenv import load_dotenv
from datetime import datetime
from src.classes.flight.schedule import Schedule
from src.classes.flight.inventory import Inventory
from src import inventory_dict, schedule_dict

load_dotenv()
schedule_file_path = os.getenv("SCHEDULE_FILE_PATH")
inventory_file_path = os.getenv("INVENTORY_FILE_PATH")


def get_schedule() -> dict[str, Schedule]:
    '''this parses the schedule sheet and returns a dict with ScheduleId as key

    :param None
    :return: dictionary of schedules with ScheduleId as key
    :rtype: dict[str, Schedule]
    '''
    schedule_df = read_csv(schedule_file_path)
    schedule_dict = {}
    for index, row in schedule_df.iterrows():
        curr_schedule = schedule_df.iloc[index].to_dict()
        curr_schedule = {k.lower(): v for k, v in curr_schedule.items()}
        schedule_dict[curr_schedule["scheduleid"]] = Schedule(**curr_schedule)
    return schedule_dict


def get_inventory() -> dict[str, Inventory]:
    '''this parses the inventory sheet and returns a dict with InventoryId as key

    :param None
    :return: dictionary of inventories with InventoryId as key
    :rtype: dict[str, Inventory]
    '''
    inv_df = read_csv(inventory_file_path)
    inv_dict = {}
    for index, row in inv_df.iterrows():
        curr_inv = inv_df.iloc[index].to_dict()
        curr_inv = {k.lower(): v for k, v in curr_inv.items()}
        inv_dict[curr_inv["inventoryid"]] = Inventory(**curr_inv)
    return inv_dict


def get_date_inventory_list_dict() -> dict[datetime, list[str]]:
    '''This function returns a dictionary of dates and inventory ids

    :param None
    :return: dictionary of dates and inventory ids
    :rtype: dict[datetime, list[str]]
    '''

    date_inventory_list_dict: dict[datetime, list[str]] = {}
    sorted_inventory_list = sorted(inventory_dict.values(), key=lambda x: datetime.strptime(
        x.departuredate + " " + schedule_dict[x.inventoryid].departuretime, "%m/%d/%Y %H:%M"))

    for inventory_obj in sorted_inventory_list:
        date_inventory_list_dict[datetime.strptime(
            inventory_obj.departuredate, "%m/%d/%Y")].append(inventory_obj.inventoryid)

    return date_inventory_list_dict
