from src.fetch_input.flight_input import get_inventory, get_schedule
from src.fetch_input.pnr_input import get_pnr_booking_input, get_pnr_passenger_input
from src.fetch_input.airport_extractor import get_airport_city_codes, get_airport_info

inventory_dict = get_inventory()
schedule_dict = get_schedule()
passenger_dict = get_pnr_passenger_input()
booking_dict = get_pnr_booking_input()
airport_city_codes_dict = get_airport_city_codes()
airport_city_info_dict = get_airport_info()
