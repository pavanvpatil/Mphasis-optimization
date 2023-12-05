from src import schedule_dict
from src import inventory_dict
from src import booking_dict
from src import passenger_dict
from src.fetch_input.pnr_input import get_pnr_passenger_input


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

def get_affected_passengers(inventory_id) -> list:
    '''
    This function returns a list of doc_id of passengers
    param inventory_id : inventory id of affected flight
    type inventory_id: str
    return list of doc_id of affected passengers
    rtype list[str]
    '''
    af_pnrs = get_affected_pnrs(inventory_id)
    af_passengers = []
    for pnr in af_pnrs:
        for passenger in passenger_dict:
            if af_pnrs[pnr].recloc == passenger_dict[passenger].recloc:
                af_passengers.append(passenger_dict[passenger].doc_id)
    return af_passengers

def rank_pnrs(inventory_id) -> list:
    '''
    This method ranks the affected pnrs as per the pnr_ranking sheet

    param  inventory_id : Inventory id of affected flight
    type inventory_id : str
    return list of doc_id of passengers ranked as per pnr_score (highest score will be the first element)
    rtype : list[str]
    '''
    cabinJ = ["A", "D", "J"]
    cabinF = ["F", "B"]
    cabinY = ["S", "V", "W", "Z", "O", "S", "T", "U", "M", "N", "Y", "E", "L"]
    affected_pnrs_list = get_affected_pnrs(inventory_id)
    affected_pnrs = {}
    for pnr in affected_pnrs_list:
        affected_pnrs[pnr] = booking_dict[pnr]
    for booking in affected_pnrs:
        curr_booking = booking_dict[booking]
        score = 0
        score = score + int(curr_booking.pax_cnt) * 50
        if curr_booking.cos_cd[0] in cabinF:
            score = score + 1700
        elif curr_booking.cos_cd[0] in cabinJ:
            score = score + 2000
        elif curr_booking.cos_cd[0] in cabinY:
            score = score + 1500
        recloc = affected_pnrs[booking].recloc

        for passenger in passenger_dict:
            if passenger_dict[passenger].recloc == recloc:
                if len(str(passenger_dict[passenger].ssr_code_cd1)) > 3:
                    score = score + 200 * (str(passenger_dict[passenger].ssr_code_cd1).count(",") + 1)
        score = score + 750 #for class

        affected_pnrs[booking].score = score
    ranked_pnrs = dict(sorted(affected_pnrs.items(), key=lambda x: x[1].score, reverse=True))

    recloc_list = [ranked_pnrs[k].recloc for k in ranked_pnrs]

    op = []
    for pnr in recloc_list:
        a = False
        for passenger in passenger_dict:
            if passenger_dict[passenger].recloc == pnr:
                a = True
                op.append(passenger)
        if not a:
            op.append("nan")  # if recloc is not found in the pnr_passenger sheet

    return op
