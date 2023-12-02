

def isAltFlightPossible(id1, *id2)->bool:
    if len(id2) > 3: #more than 3 connecting flights are not allowed
        return False
    max_dep_diff = 72 #in hours
    max_conn_diff = 12
    dep1 = id1.departure_date.split('/') + id1.departure_time.split(':') #list of format ['mm','dd','yyyy','hh','mm']
    dep2 = id2[0].departure_date.split('/') + id2.departure_time.split(':')
    dep_diff = 24*(int(dep2[1])-int(dep1[1])) + (int(dep2[3])-int(dep1[3])) + (int(dep2[4])-int(dep1[4]))/60
    for x in range(len(id2)-1):
        '''
        We calculate difference in arrival of a connecting flight and
        departure of the consecutive connecting flight and store it in 
        conn_diff
        '''
        arr2 = id2[x].arrival_date.split('/') + id2.arrival_time.split(':')
        dep2 = id2[x+1].departure_date.split('/') + id2.departure_time.split(':')
        conn_diff = 24*(int(dep2[1])-int(arr2[1])) + (int(dep2[3])-int(arr2[3])) + (int(dep2[4])-int(arr2[4]))/60
        if conn_diff<1 or conn_diff>max_conn_diff:
            return False

    if dep_diff > max_dep_diff : 
        return False
    else: 
        return True
