from src import airport_city_info_dict
import geopy.distance as geopy_distance

def get_distance_from_airport_codes(airport_code1: str, airport_code2: str) -> float:
    '''Returns the distance between two airports in kilometers
    
    :param airport_code1: the airport code of the first airport
    :param airport_code2: the airport code of the second airport
    :return: the distance between the two airports in kilometers
    :rtype: float
    '''
    try:
        lat1 = airport_city_info_dict[airport_code1].lat
        long1 = airport_city_info_dict[airport_code1].long

        lat2 = airport_city_info_dict[airport_code2].lat
        long2 = airport_city_info_dict[airport_code2].long

        return geopy_distance.geodesic((lat1, long1), (lat2, long2)).km
    except:
        return float(200)



