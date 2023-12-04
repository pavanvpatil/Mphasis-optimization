from Code.pnr_input import get_pnr_passenger_input
from Code.pnr_input import get_pnr_booking_input
from Code.get_schedule_and_inventory import get_schedule
from Code.get_schedule_and_inventory import get_inventory
from Code.get_affected_pnrs import get_affected_pnrs


pnr_passengers = get_pnr_passenger_input()
pnr_bookings = get_pnr_booking_input()
schedule_dict = get_schedule()
inv_dict = get_inventory()

op = get_affected_pnrs("INV-ZZ-1875559")

#cant test this with the current dataset, i tested it by modifying the booking sheet
print(op["FEAPID:ZZ:3417"])