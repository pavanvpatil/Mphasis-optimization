import os
from pandas import read_csv
from dotenv import load_dotenv
from src.classes.pnr.booking import Booking
from src.classes.pnr.passenger import Passenger

load_dotenv()
pnr_passenger_file_path = os.getenv("PNR_PASSENGER_FILE_PATH")
pnr_booking_file_path = os.getenv("PNR_BOOKING_FILE_PATH")


def get_pnr_passenger_input() -> dict[str, Passenger]:
    '''
    Fetches input from PNR passenger csv file and returns a dictionary of passengers with doc_id as key.

    :param None
    :return: dictionary of passengers with doc_id as key
    :rtype: dict[str, Passenger]
    '''

    try:
        pnr_passenger_df = read_csv(pnr_passenger_file_path)
    except FileNotFoundError:
        print("PNR passenger file not found")
        exit(1)

    passenger_dict = {}
    for index, row in pnr_passenger_df.iterrows():
        cur_passenger = pnr_passenger_df.iloc[index].to_dict()
        cur_passenger = {k.lower(): v for k, v in cur_passenger.items()}
        cur_passenger["doc_id"] = str(int(cur_passenger["doc_id"]))
        passenger_dict[cur_passenger["doc_id"]] = Passenger(**cur_passenger)
    return passenger_dict


def get_pnr_booking_input() -> dict[str, Booking]:
    '''
    Fetches input from PNR booking csv file and returns a dictionary of bookings with booking_key as key.

    :param None
    :return: dictionary of bookings with booking_key as key (generated using recloc, carrier_cd and flt_num)
    :rtype: dict[str, Booking]
    '''

    try:
        pnr_booking_df = read_csv(pnr_booking_file_path)
    except FileNotFoundError:
        print("PNR booking file not found")
        exit(1)

    booking_dict = {}
    for index, row in pnr_booking_df.iterrows():
        cur_booking = pnr_booking_df.iloc[index].to_dict()
        cur_booking = {k.lower(): v for k, v in cur_booking.items()}
        booking_key = str(cur_booking["recloc"]) + ":" + \
            str(cur_booking["carrier_cd"]) + ":" + str(cur_booking["flt_num"])
        booking_dict[booking_key] = Booking(**cur_booking)
    return booking_dict
