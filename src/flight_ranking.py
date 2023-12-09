from datetime import datetime,timedelta
import pandas as pd
from src import inventory_dict
from src import schedule_dict
from src import airport_city_codes_dict
from src.classes.flight.schedule import Schedule
from src.classes.flight.inventory import Inventory


def city_pairs_check(
    inv_id_affected: str,
    inv_id_proposed_dep: str,
    inv_id_proposed_arr: str
) -> int:
    '''Returns calculated scores for airport pairs

    :param inv_id_affected: Inventory ID of the affected flight
    :param type: str
    :param inv_id_proposed_dep: Inventory ID of the first flight of the proposed sequence
    :param type: str
    :param inv_id_proposed_arr: Inventory ID of the last flight of the proposed sequence
    :param type: str
    :return: points scored for the airport pair
    :rtype: int
    '''

    depart_airport_affected = inventory_dict[inv_id_affected].departureairport
    arrival_airport_affected = inventory_dict[inv_id_affected].arrivalairport

    depart_airport_proposed = inventory_dict[inv_id_proposed_dep].departureairport
    arrival_airport_proposed = inventory_dict[inv_id_proposed_arr].arrivalairport

    points = 0

    if depart_airport_affected == depart_airport_proposed and arrival_airport_affected == arrival_airport_proposed:
        points += 40
    elif airport_city_codes_dict[arrival_airport_affected] == airport_city_codes_dict[arrival_airport_proposed] or airport_city_codes_dict[depart_airport_affected] == airport_city_codes_dict[depart_airport_proposed]:
        points += 30
    else:
        points += 20

    return points


def find_date_time_difference(
    inv_id_affected: str,
    inv_id_proposed_dep: str,
    inv_id_proposed_arr: str
) -> tuple[float]:
    '''Returns the difference in arrival and departure time of the affected flight and the proposed sequence in hours

    :param inv_id_affected: Inventory ID of the affected flight
    :param type: str
    :param inv_id_proposed_dep: Inventory ID of the first flight of the proposed sequence
    :param type: str
    :param inv_id_proposed_arr: Inventory ID of the last flight of the proposed sequence
    :param type: str
    :return: tuple of the difference in arrival and departure time of the affected flight and the proposed sequence in hours
    :rtype: tuple[float]
    '''

    schedule_id_affected = inventory_dict[inv_id_affected].scheduleid
    schedule_id_proposed_dep = inventory_dict[inv_id_proposed_dep].scheduleid
    schedule_id_proposed_arr = inventory_dict[inv_id_proposed_arr].scheduleid

    date_time_affected_departure = inventory_dict[inv_id_affected].departuredate + \
        " " + \
        schedule_dict[schedule_id_affected].departuretime  # format mm/dd/yyyy hh:mm
    date_time_proposed_departure = inventory_dict[inv_id_proposed_dep].departuredate + \
        " " + schedule_dict[schedule_id_proposed_dep].departuretime

    date_time_affected_departure = datetime.strptime(
        date_time_affected_departure, "%m/%d/%Y %H:%M")
    date_time_proposed_departure = datetime.strptime(
        date_time_proposed_departure, "%m/%d/%Y %H:%M")

    departure_diff = (date_time_proposed_departure -
                      date_time_affected_departure).total_seconds()/3600

    date_time_affected_arrival = inventory_dict[inv_id_affected].arrivaldate + \
        " " + \
        schedule_dict[schedule_id_affected].arrivaltime  # format mm/dd/yyyy hh:mm
    date_time_proposed_arrival = inventory_dict[inv_id_proposed_arr].arrivaldate + \
        " " + schedule_dict[schedule_id_proposed_arr].arrivaltime

    date_time_affected_arrival = datetime.strptime(
        date_time_affected_arrival, "%m/%d/%Y %H:%M")
    date_time_proposed_arrival = datetime.strptime(
        date_time_proposed_arrival, "%m/%d/%Y %H:%M")

    arrival_diff = (date_time_proposed_arrival -
                    date_time_affected_arrival).total_seconds()/3600

    return (arrival_diff, departure_diff)


def connection_flight_check(
    inv_id_affected: str,
    inv_id_proposed: list[str],
) -> bool:
    '''This function checks if the proposed sequence of flights is a valid connecting flight sequence

    :param inv_id_affected: Inventory ID of the affected flight
    :param type: str
    :param inv_id_proposed: Inventory ID of the proposed sequence of flights
    :param type: list[str]
    :return: True if the proposed sequence of flights is a valid connecting flight sequence, False otherwise
    :rtype: bool
    '''
    # NOTE:  Max 3 connections not specified, commenting this out
    #       Keep it commented until further ruleset changes

    # if len(id2) > 3: # more than 3 connecting flights are not allowed
    #     return False

    max_dep_diff_hours = 72
    min_conn_diff_hours = 1
    max_conn_diff_hours = 12

    time_diff = find_date_time_difference(
        inv_id_affected=inv_id_affected,
        inv_id_proposed_dep=inv_id_proposed[0],
        inv_id_proposed_arfromr=inv_id_proposed[-1]
    )

    if time_diff[1] > max_dep_diff_hours:
        return False
    else:

        for idx in range(len(inv_id_proposed)-1):
            sch_id_1 = inventory_dict[inv_id_proposed[idx]].scheduleid
            sch_id_2 = inventory_dict[inv_id_proposed[idx+1]].scheduleid

            cur_flight_arr_time = inventory_dict[inv_id_proposed[idx]
                                                 ].departuredate + " " + schedule_dict[sch_id_1].departuretime
            next_flight_dep_time = inventory_dict[inv_id_proposed[idx+1]
                                                  ].departuredate + " " + schedule_dict[sch_id_2].departuretime

            date_time_arrive = datetime.strptime(
                cur_flight_arr_time, "%m/%d/%Y %H:%M")
            date_time_depart = datetime.strptime(
                next_flight_dep_time, "%m/%d/%Y %H:%M")

            conn_diff_hours = (date_time_depart -
                               date_time_arrive).total_seconds()/3600

            if conn_diff_hours < min_conn_diff_hours or conn_diff_hours > max_conn_diff_hours:
                return False

        return True


def sta_std_check(inv_id_affected: str, inv_id_proposed: list[str]) -> int:
    '''This method is used to score the proposed sequence of flights based on the difference 
    between the arrival and departure time of the affected flight and the proposed sequence of flights

    :param inv_id_affected: Inventory ID of the affected flight
    :param type: str
    :param inv_id_proposed: Inventory ID of the proposed sequence of flights
    :param type: list[str]
    :return: points scored for the proposed sequence of flights
    :rtype: int
    '''
    points = 0

    time_diff = find_date_time_difference(
        inv_id_affected=inv_id_affected,
        inv_id_proposed_dep=inv_id_proposed[0],
        inv_id_proposed_arr=inv_id_proposed[-1]
    )

    arrive_diff = time_diff[0]
    dep_diff = time_diff[1]

    if arrive_diff <= 6:
        points += 70
    elif arrive_diff <= 12:
        points += 50
    elif arrive_diff <= 24:
        points += 40
    else:
        points += 30

    if dep_diff <= 6:
        points += 70
    elif dep_diff <= 12:
        points += 50
    elif dep_diff <= 24:
        points += 40
    else:
        points += 30

    return points


def equipment_check(inv_id_affected: str, inv_id_proposed: list[str]) -> bool:
    if inventory_dict[inv_id_affected].aircrafttype == inventory_dict[inv_id_proposed[0]].aircrafttype:
        return True
    else:
        return False



def flight_date_comparator(inv_id_1: Inventory, inv_id_2: Inventory) -> bool:
    sched_id_1 = inv_id_1.scheduleid
    sched_id_2 = inv_id_2.scheduleid


    date_time_1 = inv_id_1.departuredate + \
        " " + \
        schedule_dict[inv_id_1.scheduleid].departuretime

    date_time_depart_1 = datetime.strptime(
                date_time_1, "%m/%d/%Y %H:%M")

    date_time_2 = inv_id_2.departuredate + \
        " " + \
        schedule_dict[inv_id_2.scheduleid].departuretime


    date_time_depart_2 = datetime.strptime(
                date_time_2, "%m/%d/%Y %H:%M")

'''
    Need to be tested
'''
def find_alternate_flight_on_day(inventory_obj: Inventory, date_dictionary: dict, schedule_dict: dict, inv_dict: dict) -> list[str]:

    affected_date_string = inventory_obj.departuredate

    originalTimeOfDeparture = datetime.strptime(schedule_dict[inventory_obj.scheduleid].departuretime,"%H:%M")
    

    affected_date = datetime.strptime(affected_date_string,"%m/%d/%Y")
    
    affected_date_string = inventory_obj.departuredate
    suggested_date_list = []
    for x in range(4):
        append_this = (affected_date + timedelta(days=x)).strftime("%m/%d/%Y")
        if append_this in date_dictionary.keys():
            suggested_date_list.append(append_this)

    suggested_inventory_ids = []


    if len(suggested_date_list) == 3:
        for date in suggested_date_list[0:-1]:
            suggested_inventory_ids.extend(date_dictionary[date])

        #do binary search until the stipulated
        last_day = date_dictionary[suggested_date_list[-1]]
        high = len(last_day)-1
        low  = 0
        while(not low == high):
            mid = (low+high)//2
            midval = schedule_dict[last_day[mid]].get_time_of_departure()

            if(mid == low):
                break

            if midval < originalTimeOfDeparture:
                low = mid
            else:
                high=mid

        suggested_inventory_ids = suggested_inventory_ids+last_day[:low]
    return suggested_inventory_ids


