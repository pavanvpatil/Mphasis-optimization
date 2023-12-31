from src import inventory_dict
from src import booking_dict
from src import passenger_dict
from src.gui.gui import pnr_ranking_values_obj


def get_affected_pnrs(inventory_id: str) -> set[str]:
    '''This method returns a list of affected pnrs for a given inventory id

    :param inventory_id: Inventory ID of the affected flight
    :type inventory_id: str
    :return: set of affected pnrs
    :rtype: set[str] 
    '''

    affected_pnrs = set()
    dep_key = inventory_dict[inventory_id].dep_key[0: -2]

    for booking_id in booking_dict:
        if booking_dict[booking_id].dep_key == dep_key:
            affected_pnrs.add(booking_dict[booking_id].recloc)

    return affected_pnrs


def get_affected_bookings(inventory_id: str) -> set[str]:
    '''This method returns a list of affected bookings for a given inventory id

    :param inventory_id: Inventory ID of the affected flight
    :type inventory_id: str
    :return: set of affected bookings
    :rtype: set[str] 
    '''

    affected_bookings = set()
    dep_key = inventory_dict[inventory_id].dep_key[0: -2]

    for booking_id in booking_dict:
        if booking_dict[booking_id].dep_key == dep_key:
            affected_bookings.add(booking_id)

    return affected_bookings


def get_affected_passengers(inventory_id) -> list[str]:
    '''
    This function returns a list of doc_id of passengers
    param inventory_id : inventory id of affected flight
    type inventory_id: str
    return list of doc_id of affected passengers
    rtype list[str]
    '''
    affected_pnrs = get_affected_pnrs(inventory_id)
    affected_passengers_doc_ids = []

    for passenger_doc_id in passenger_dict:
        if passenger_dict[passenger_doc_id].recloc in affected_pnrs:
            affected_passengers_doc_ids.append(passenger_doc_id)

    return affected_passengers_doc_ids


def get_pnr_score_dict(inventory_id) -> dict[str, int]:
    '''
    This method returns a dictionary of pnr_score of affected pnrs for a given inventory id

    :param inventory_id: Inventory ID of the affected flight
    :type inventory_id: str
    :return: dictionary of pnr_score of affected pnrs
    :rtype: dict[str, int]
    '''

    cabinB = ["BusinessClass"]
    cabinF = ["FirstClass"]
    cabinPE = ["PremiumEconomyClass"]
    cabinE = ["EconomyClass"]

    pnr_score_dict = {}
    affected_booking_ids = get_affected_bookings(inventory_id)

    for booking_id in affected_booking_ids:
        curr_booking = booking_dict[booking_id]
        pnr_score = 0

        pnr_score = pnr_score + \
            int(curr_booking.pax_cnt) * pnr_ranking_values_obj.pax_cnt_score

        if curr_booking.cos_cd in cabinF:
            pnr_score = pnr_score + pnr_ranking_values_obj.first_class_score
        elif curr_booking.cos_cd in cabinB:
            pnr_score = pnr_score + pnr_ranking_values_obj.business_class_score
        elif curr_booking.cos_cd in cabinPE:
            pnr_score = pnr_score + \
                pnr_ranking_values_obj.premium_eco_class_score
        elif curr_booking.cos_cd in cabinE:
            pnr_score = pnr_score + pnr_ranking_values_obj.eco_class_score
        pnr = curr_booking.recloc

        pnr_score = pnr_score + 750

        pnr_score_dict[pnr] = pnr_score

    return pnr_score_dict


def get_ranked_affected_passenger_doc_ids(inventory_id) -> list[str]:
    '''
    This method ranks the affected pnrs as per the pnr_ranking sheet

    param  inventory_id : Inventory id of affected flight
    type inventory_id : str
    return list of doc_id of passengers ranked as per pnr_score (highest score will be the first element)
    rtype : list[str]
    '''
    pnr_score_dict = get_pnr_score_dict(inventory_id)

    affected_passengers_dict = {}
    for passenger_doc_id in passenger_dict:
        passenger = passenger_dict[passenger_doc_id]
        if passenger.recloc in pnr_score_dict:
            pnr_score = pnr_score_dict[passenger.recloc]
            ssr_score = 0
            if len(str(passenger.ssr_code_cd1)) > 3:
                ssr_score = pnr_ranking_values_obj.ssr_score * \
                    (str(passenger.ssr_code_cd1).count(
                        ",") + 1)
            if len(str(passenger.tierlevel)) > 2:
                if passenger.tierlevel == "Silver":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_silver
                elif passenger.tierlevel == "Gold":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_gold
                elif passenger.tierlevel == "Platinum":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_platinum
                elif passenger.tierlevel == "PresidentialPlatinum":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_pplatinum
            affected_passengers_dict[passenger_doc_id] = ssr_score + pnr_score

    ranked_affected_passenger_doc_ids = sorted(affected_passengers_dict.keys(),
                                               key=lambda x: affected_passengers_dict[x], reverse=True)
    return ranked_affected_passenger_doc_ids


def get_avg_pnr_score(inventory_id) -> float:
    '''
    This method returns the average pnr score of passengers of affected bookings of a given inventory

    :param inventory_id: Inventory id of affected flight
    :type inventory_id: str
    :return average pnr score of passengers of affected bookings of a given inventory
    :rtype float
    '''

    pnr_score_dict = get_pnr_score_dict(inventory_id)

    num_passengers = 0
    total_pnr_score = 0
    for passenger_doc_id in passenger_dict:
        passenger = passenger_dict[passenger_doc_id]
        if passenger.recloc in pnr_score_dict:
            num_passengers = num_passengers + 1
            pnr_score = pnr_score_dict[passenger.recloc]
            ssr_score = 0
            if len(str(passenger.ssr_code_cd1)) > 3:
                ssr_score = pnr_ranking_values_obj.ssr_score * \
                    (str(passenger.ssr_code_cd1).count(
                        ",") + 1)
            if len(str(passenger.tierlevel)) > 2:
                if passenger.tierlevel == "Silver":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_silver
                elif passenger.tierlevel == "Gold":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_gold
                elif passenger.tierlevel == "Platinum":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_platinum
                elif passenger.tierlevel == "PresidentialPlatinum":
                    ssr_score = ssr_score + pnr_ranking_values_obj.loyalties_pplatinum
            total_pnr_score = total_pnr_score + ssr_score + pnr_score

    return float(total_pnr_score/num_passengers)
