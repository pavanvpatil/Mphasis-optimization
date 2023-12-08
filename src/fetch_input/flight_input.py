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



def append_dict(inventory_obj: Inventory, *date_dictionary: dict) -> dict:
    '''
    Takes in inventory_id string as input and appends it to a dictionary of dates & airports
    {
        Date1:  {
                    Airport1: [inv_id_1, inv_id_2, ...]
                    Airport2: [inv_id_3, inv_id_4, ...]
                }
        Date2:  {
                    Airport2: [inv_id_5, inv_id_6, ...]
                    Airport4: [inv_id_7, inv_id_8, ...]
                }
        Date3:  {
                    Airport5: [inv_id_9, inv_id_10, ...]
                    Airport6: [inv_id_11, inv_id_12, ...]
                }
        .
        .
        .

    }
    A calendar of sorts
    '''

    dep_date = inventory_obj.departuredate
    departure_city_code = inventory_obj.departureairport

    dep_date_time_string = inventory_obj.departuredate + \
        " " + \
        schedule_dict[inventory_obj.schdeuleid].departuretime

    dep_date_time = datetime.strptime(dep_date_time_string,"%m/%d/%Y %H:%M")

    if(dep_date in date_dictionary.keys):
            inv_id_list = date_dictionary[dep_date]
            
            idx_l = 0
            idx_r = len(inv_id_list) - 1
            

            while (not idx_l == idx_r):
                idx_mid = (idx_l + idx_r)//2
                mid_inv_id = inv_id_list[idx_mid]

                mid_date_time_string = inv_dict[mid_inv_id].departuredate + \
                " " + \
                schedule_dict[inv_dict[mid_inv_id].schdeuleid].departuretime

                mid_date_time = datetime.strptime(mid_date_time_string,"%m/%d/%Y %H:%M")

                if dep_date_time < mid_date_time:
                    idx_r = idx_mid
                else:
                    idx_l = idx_mid
            
            final_date_time_string = inv_dict[l_inv_id].departuredate + \
                " " + \
                schedule_dict[inv_dict[l_inv_id].schdeuleid].departuretime

            final_date_time = datetime.strptime(final_date_time_string,"%m/%d/%Y %H:%M")

            if dep_date_time < final_date_time:
                date_dictionary[dep_date].insert(idx_l, inventory_obj.inventoryid)
            else:
                date_dictionary[dep_date].insert(idx_l+1, inventory_obj.inventoryid)

            date_dictionary[dep_date].append(inventory_obj.inventory_id)
    else:
        date_dictionary[dep_date] = [inventory_obj.inventory_id]

    return date_dictionary
