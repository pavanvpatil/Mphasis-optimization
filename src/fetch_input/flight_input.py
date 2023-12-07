import os
from pandas import read_csv
from dotenv import load_dotenv
from datetime import datetime
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


def append_dict(date : str,inventoryId :str,*dateDictionary:dict) -> dict:
    input_date = datetime.strptime(date,"%m/%d/%y")
    if(input_date in dateDictionary.keys):
        dateDictionary[input_date].append(inventoryId)
    else:
        dateDictionary[input_date] = [inventoryId]
    return dateDictionary