from Shedule.get_schedule_and_inventory import get_inventory
from Shedule.get_schedule_and_inventory import get_schedule
from PNR.pnr_input import get_pnr_booking_input

import PNR.pnr_input




def get_affected_pnrs(InventoryId) -> dict:
    #gets all affected pnr bookings with inventory id and returns a dict with RECLOC:CARRIER_CD:FLT_NO as key and object of booking class as value
    #it checks flt_number and carrier_cd
    #InventoryId is the inventoryid of canceled flight

    inventory_dict = get_inventory()
    schedule_dict = get_schedule()
    affected_pnrs = {}
    sched_id = inventory_dict[InventoryId].ScheduleId
    fno = schedule_dict[sched_id].FlightNumber
    carrier_code = schedule_dict[sched_id].CarrierCode
    pnr_booking = get_pnr_booking_input()
    for currBooking in pnr_booking:
        if (pnr_booking[currBooking].carrier_cd == carrier_code and pnr_booking[currBooking].flt_num == fno):
            affected_pnrs[currBooking] = pnr_booking[currBooking]
    return affected_pnrs



