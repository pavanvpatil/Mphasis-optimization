import csv
import os
from pandas import read_csv
from dotenv import load_dotenv
from Shedule.shedule import Schedule
from Shedule.Inventory import Inventory

load_dotenv()
shedule_file_path = os.getenv("SHEDULE_FILE_PATH")
inventory_file_path = os.getenv("INVENTORY_FILE_PATH")

def get_schedule() -> dict:

    #this parses the shedule sheet and returns a dict with ScheduleId as the key
    shedule_df = read_csv(shedule_file_path)
    shedule_dict = {}
    for index, row in shedule_df.iterrows():
        currShedule = shedule_df.iloc[index].to_dict()
        shedule_dict[currShedule["ScheduleID"]] = Schedule(**currShedule)
    return shedule_dict

def get_inventory() -> dict:
    #this parses the inventory sheet and returns a dict with InventoryId as key
    inv_df = read_csv(inventory_file_path)
    inv_dict = {}
    for index, row in inv_df.iterrows():
        currInv = inv_df.iloc[index].to_dict()
        inv_dict[currInv["InventoryId"]] = Inventory(**currInv)
    return inv_dict