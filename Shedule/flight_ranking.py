from datetime import datetime

def isAltFlightPossible(id1, *id2)->bool:
    if len(id2) > 3: # more than 3 connecting flights are not allowed
        return False
    max_dep_diff = 72 # in hours
    max_conn_diff = 12
    dep1 = id1.departure_date +" "+ id1.departure_time # format mm/dd/yyyy hh:mm
    dep2 = id2[0].departure_date +" "+ id2[0].departure_time
    # converting the string input to date
    start_date = datetime.strptime(dep1, "%m/%d/%Y %H:%M")
    end_date = datetime.strptime(dep2, "%m/%d/%Y %H:%M")
 
    # calculating the difference in dates
    dep_diff = (end_date-start_date).total_seconds()/3600
    for x in range(len(id2)-1):
        '''
        We calculate difference in arrival of a connecting flight and
        departure of the consecutive connecting flight for all connecting flights and store it in 
        conn_diff
        '''
        arr2 = id2[x].arrival_date + " " + id2[x].arrival_time
        dep2 = id2[x+1].departure_date + " " + id2[x+1].departure_time
        start_date = datetime.strptime(arr2, "%m/%d/%Y %H:%M")
        end_date = datetime.strptime(dep2, "%m/%d/%Y %H:%M")
        conn_diff = (end_date-start_date).total_seconds()/3600
        if conn_diff<1 or conn_diff>max_conn_diff:
            return False

    if dep_diff > max_dep_diff : 
        return False
    else: 
        return True
