import os
import json
from pandas import read_csv
from dotenv import load_dotenv

from src.classes.flight.schedule import Schedule
from src.classes.flight.inventory import Inventory

load_dotenv()
schedule_file_path = os.getenv("SCHEDULE_FILE_PATH")
inventory_file_path = os.getenv("INVENTORY_FILE_PATH")


def get_schedule() -> dict[str, Schedule]:
    '''this parses the schedule sheet and returns a dict with ScheduleId as key

    :param None
    :return: dictionary of schedules with ScheduleId as key
    :rtype: dict[str, Schedule]
    '''

    try:
        schedule_df = read_csv(schedule_file_path)
    except FileNotFoundError:
        print("Schedule file not found")
        exit(1)

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

    try:
        inv_df = read_csv(inventory_file_path)
    except FileNotFoundError:
        print("Inventory file not found")
        exit(1)

    inv_dict = {}
    for index, row in inv_df.iterrows():
        curr_inv = inv_df.iloc[index].to_dict()
        curr_inv = {k.lower(): v for k, v in curr_inv.items()}
        curr_inv['fc_cd'] = json.loads(curr_inv['fc_cd'].replace("'", '"'))
        curr_inv['bc_cd'] = json.loads(curr_inv['bc_cd'].replace("'", '"'))
        curr_inv['pc_cd'] = json.loads(curr_inv['pc_cd'].replace("'", '"'))
        curr_inv['ec_cd'] = json.loads(curr_inv['ec_cd'].replace("'", '"'))
        inv_dict[curr_inv["inventoryid"]] = Inventory(**curr_inv)
    return inv_dict
