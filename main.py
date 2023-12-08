from src import passenger_dict, booking_dict, schedule_dict, inventory_dict
from src.rank_pnrs import get_affected_passengers
from src.fetch_input.airport_extractor import get_airport_info
from src.flight_geo import get_distance_from_airport_codes


# print(rank_pnrs("INV-ZZ-1875559"))

# print(get_airport_info())

print(get_distance_from_airport_codes("HBX", "DEL"))