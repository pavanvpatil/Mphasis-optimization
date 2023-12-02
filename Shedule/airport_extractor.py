
airport = {} #dictionary having the airport codes as a key with city names as values  
inventory = {} #dictionatry of objects with inventory id as key
def cityPairsCheck(id1:str, id2:str) -> int: #will return calculated scores
    arrivalAirport1 = inventory[id1].ArrivalAirport
    arrivalAirport2 = inventory[id2].ArrivalAirport
    departAirport1 = inventory[id1].DepartureAirport
    departAirport2 = inventory[id2].DepartureAirport
    points = 0
    #assuming data to be standardized
    if arrivalAirport1 == arrivalAirport2 and departAirport1 == departAirport2:
        points+= 40
    elif  airport[arrivalAirport1]== airport[arrivalAirport2] and airport[departAirport1]== airport[departAirport2]:
        points+=30
    else:   
        points+=20
    
    return points

def equipmentCheck(id1:str,id2:str) -> int:
    if inventory[id1].AircraftType == inventory[id2].AircraftType:
        return 50
    return 0



