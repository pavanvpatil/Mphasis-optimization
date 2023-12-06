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
    dep_date = inventory_dict[inventory_id].departuredate


    for curr_booking in booking_dict:
        if booking_dict[curr_booking].carrier_cd == carrier_code and booking_dict[curr_booking].flt_num == fno and booking_dict[curr_booking].dep_dt == dep_date:
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
    af_pnrs_list = get_affected_pnrs(inventory_id)
    af_pnrs = set()
    for pnr in af_pnrs_list:
        af_pnrs.add(booking_dict[pnr].recloc)
    print(af_pnrs)
    af_passengers = []
    # for pnr in af_pnrs:
    #     for passenger in passenger_dict:
    #         if booking_dict[pnr].recloc == passenger_dict[passenger].recloc:
    #             af_passengers.append(passenger_dict[passenger].doc_id)
    for passenger in passenger_dict:
        if passenger_dict[passenger].recloc in af_pnrs:
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
    recloc_score_dict = {}
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
        score = score + 750  # for class
        recloc_score_dict[recloc] = score
    aff_passengers_dict = {}
    for passenger in passenger_dict:
        if passenger_dict[passenger].recloc in recloc_score_dict:
            score = recloc_score_dict[passenger_dict[passenger].recloc]
            ssr_score = 0
            if len(str(passenger_dict[passenger].ssr_code_cd1)) > 3:
                ssr_score = 200 * (str(passenger_dict[passenger].ssr_code_cd1).count(",") + 1)
            aff_passengers_dict[passenger_dict[passenger].doc_id] = ssr_score + score
    op = sorted(aff_passengers_dict.keys(), key=lambda x: aff_passengers_dict[x], reverse=True)
    return op
