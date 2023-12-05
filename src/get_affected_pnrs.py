from src import schedule_dict
from src import inventory_dict
from src import booking_dict


def get_affected_pnrs(inventory_id: str) -> list[str]:
    '''This method returns a list of affected pnrs for a given inventory id

    :param inventory_id: Inventory ID of the affected flight
    :type inventory_id: str
    :return: list of affected pnrs
    :rtype: list[str] 
    '''

    affected_pnrs = []
    schedule_id = inventory_dict[inventory_id].scheduleid
    fno = schedule_dict[schedule_id].flightnumber
    carrier_code = schedule_dict[schedule_id].carriercode

    for curr_booking in booking_dict:
        if booking_dict[curr_booking].carrier_cd == carrier_code and booking_dict[curr_booking].flt_num == fno:
            affected_pnrs.append(curr_booking)

    return affected_pnrs
