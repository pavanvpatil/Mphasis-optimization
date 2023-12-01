from PNR.pnr_input import get_pnr_passenger_input
from PNR.pnr_input import get_pnr_booking_input
from Shedule.get_schedule_and_inventory import get_inventory
from Shedule.get_schedule_and_inventory import get_schedule


pnr_passengers = get_pnr_passenger_input()
pnr_bookings = get_pnr_booking_input()
schedule_dict = get_schedule()
print(schedule_dict)
