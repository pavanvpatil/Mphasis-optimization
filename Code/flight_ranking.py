from datetime import datetime

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#NOTE: CALL FUNCTIONS GET_INV_DICT AND GET_SCHED_DICT
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#Global
#isStopOver = False (bool)
#==============================================================================================================================================

#Returns calculated scores for airport pairs
def cityPairsCheck(inv_id_affected: str, *inv_id_proposed) -> int:

    departAirport1 = inv_dict[inv_id_affected].DepartureAirport
    arrivalAirport1 = inv_dict[inv_id_affected].ArrivalAirport

    departAirport2 = inv_dict[inv_id_proposed[0]].DepartureAirport
    arrivalAirport2 = inv_dict[inv_id_proposed[-1]].ArrivalAirport

    points = 0

    #assuming data to be standardized
    if arrivalAirport1 == arrivalAirport2 and departAirport1 == departAirport2:
        points += 40
    elif city[arrivalAirport1] == city[arrivalAirport2] or city[departAirport1] == city[departAirport2]:
        points += 30
    else:
        points += 20


    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #NOTE: The final else condition provides 20 points even if City1 and City2 are different
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    return points

#==============================================================================================================================================

def findDateTimeDifference(inv_id_affected, *inv_id_proposed) -> tuple:
    sch_id_affected = inv_dict[inv_id_affected].ScheduleID
    sch_id_proposed_0 = inv_dict[inv_id_proposed[0]].ScheduleID     #Takes into account the first flight of the proposed sequence
    sch_id_proposed_l = inv_dict[inv_id_proposed[-1]].ScheduleID     #Takes into account the last flight of the proposed sequence

    dt_affected_depart = inv_dict[inv_id_affected].DepartureDate + " " + schedule_dict[sch_id_affected].DepatureTime # format mm/dd/yyyy hh:mm
    dt_proposed_depart = inv_dict[inv_id_proposed[0]].DepartureDate + " " + schedule_dict[sch_id_proposed_0].DepatureTime

    # converting the string input to date
    date_time_affected_d = datetime.strptime(dt_affected_depart, "%m/%d/%Y %H:%M")
    date_time_proposed_d = datetime.strptime(dt_proposed_depart, "%m/%d/%Y %H:%M")

    # calculating the difference in dates
    dep_diff = (date_time_proposed - date_time_affected).total_seconds()/3600

    dt_affected_arrive = inv_dict[inv_id_affected].ArrivalDate + " " + schedule_dict[sch_id_affected].ArrivalTime # format mm/dd/yyyy hh:mm
    dt_proposed_arrive = inv_dict[inv_id_proposed[-1]].ArrivalDate + " " + schedule_dict[sch_id_proposed_l].ArrivalTime

    # converting the string input to date
    date_time_affected_a = datetime.strptime(dt_affected_arrive, "%m/%d/%Y %H:%M")
    date_time_proposed_a = datetime.strptime(dt_proposed_arrive, "%m/%d/%Y %H:%M")

    # calculating the difference in dates
    arrive_diff = (date_time_proposed - date_time_affected).total_seconds()/3600

    return (arrive_diff, dep_diff)

#==============================================================================================================================================

def connectionFlightCheck(inv_id_affected: str, *inv_id_proposed) -> bool:
    #NOTE:  Max 3 connections not specified, commenting this out
    #       Keep it commented until further ruleset changes

    # if len(id2) > 3: # more than 3 connecting flights are not allowed
    #     return False

    max_dep_diff = 72 # in hours
    min_conn_diff = 1
    max_conn_diff = 12

    time_diff = findDateTimeDifference(inv_id_affected, *inv_id_proposed)

    if time_diff[1] > max_dep_diff:
        return False
    else:

        for idx in range(len(inv_id_proposed)-1):
            '''
            We calculate difference in arrival of a connecting flight and
            departure of the consecutive connecting flight for each connecting flights and store it in
            conn_diff.
            RULE: Connecting Flight Time differences must be between 1 and 12 hours
            '''
            sch_id_1 = inv_dict[inv_id_proposed[idx]].ScheduleID
            sch_id_2 = inv_dict[inv_id_proposed[idx+1]].ScheduleID

            fl_arrival_time = inv_dict[inv_id_proposed[idx]].DepartureDate + " " + schedule_dict[sch_id_1].DepatureTime
            nxt_depart_time = inv_dict[inv_id_proposed[idx+1]].DepartureDate + " " + schedule_dict[sch_id_2].DepatureTime

            date_time_arrive = datetime.strptime(fl_arrival_time, "%m/%d/%Y %H:%M")
            date_time_depart = datetime.strptime(nxt_depart_time, "%m/%d/%Y %H:%M")

            conn_diff = (date_time_depart - date_time_arrive).total_seconds()/3600

            if conn_diff < min_conn_diff or conn_diff > max_conn_diff:
                return False

        return True

#==============================================================================================================================================

def STA_STD_Check(inv_id_affected: str, *inv_id_proposed) -> int:

    points = 0

    time_diff = findDateTimeDifference(inv_id_affected, *inv_id_proposed)

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

#==============================================================================================================================================

def equipmentCheck(inv_id_affected: str, inv_id_proposed) -> bool:
    if inv_dict[inv_id_affected].AircraftType == inv_dict[inv_id_proposed[0]].AircraftType:
        return True
    else
        return False
