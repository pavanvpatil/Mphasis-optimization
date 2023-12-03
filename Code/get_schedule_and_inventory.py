import csv
import os
from pandas import read_csv
from dotenv import load_dotenv
from classes.Schedule.schedule import Schedule
from classes.Schedule.inventory import Inventory

load_dotenv()
schedule_file_path = os.getenv("SCHEDULE_FILE_PATH")
inventory_file_path = os.getenv("INVENTORY_FILE_PATH")

def get_schedule() -> dict:

    #this parses the schedule sheet and returns a dict with ScheduleId as the key
    schedule_df = read_csv(schedule_file_path)
    schedule_dict = {}

    

    for index, row in schedule_df.iterrows():
        currSchedule = schedule_df.iloc[index].to_dict()
        # ------ convert the keys to lowercase ------
        schedule_dict[currShedule["ScheduleID"]] = Schedule(**currSchedule)
    return schedule_dict

def get_inventory() -> dict:
    #this parses the inventory sheet and returns a dict with InventoryId as key
    inv_df = read_csv(inventory_file_path)
    inv_dict = {}

    

    for index, row in inv_df.iterrows():
        currInv = inv_df.iloc[index].to_dict()
        # ------ convert the keys to lowercase ------
        inv_dict[currInv["InventoryId"]] = Inventory(**currInv)
    return inv_dict
