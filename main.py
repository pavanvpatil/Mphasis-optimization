# from src import passenger_dict, booking_dict, schedule_dict, inventory_dict
# from src.rank_pnrs import get_affected_passengers
# from src.fetch_input.airport_extractor import get_airport_info
# from src.flight_geo import get_distance_from_airport_codes

from src import *
from src.fetch_input.flight_input import append_dict
from src.flight_ranking import find_alternate_flight_on_day


# print(rank_pnrs("INV-ZZ-1875559"))

# print(get_airport_info())

# print(get_distance_from_airport_codes("HBX", "DEL"))

schedule_dict = get_schedule()
inv_dict = get_inventory()

date_dictionary = {}
i = 0
for inv_id in inv_dict:
    if i < 100:
        append_dict(inv_dict[inv_id], date_dictionary, schedule_dict, inv_dict)
        print(inv_id)
    i += 1

list_of_alt_flights = find_alternate_flight_on_day(inv_dict["INV-ZZ-1875559"], date_dictionary, schedule_dict, inv_dict)
print(list_of_alt_flights)
