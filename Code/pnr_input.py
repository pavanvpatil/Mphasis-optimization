import os
from pandas import read_csv
from dotenv import load_dotenv
from Code.classes.PNR.passenger import Passenger
from Code.classes.PNR.booking import Booking

load_dotenv()
pnr_passenger_file_path = os.getenv("PNR_PASSENGER_FILE_PATH")
pnr_booking_file_path = os.getenv("PNR_BOOKING_FILE_PATH")


def get_pnr_passenger_input() -> dict:
    '''
    Fetches input from PNR passenger csv file and returns a dictionary of passengers with doc_id as key.
    '''
    pnr_passenger_df = read_csv(pnr_passenger_file_path)
    passenger_dict = {}
    for index, row in pnr_passenger_df.iterrows():
        cur_passenger = pnr_passenger_df.iloc[index].to_dict()
        cur_passenger = {k.lower(): v for k, v in cur_passenger.items()}
        passenger_dict[cur_passenger["doc_id"]] = Passenger(**cur_passenger)
    return passenger_dict


def get_pnr_booking_input() -> dict:
    '''
    Fetches input from PNR booking csv file and returns a dictionary of bookings with booking_key as key.
    '''
    pnr_booking_df = read_csv(pnr_booking_file_path)
    booking_dict = {}
    for index, row in pnr_booking_df.iterrows():
        cur_booking = pnr_booking_df.iloc[index].to_dict()
        cur_booking = {k.lower(): v for k, v in cur_booking.items()}
        booking_key = str(cur_booking["recloc"]) + ":" + \
            str(cur_booking["carrier_cd"]) + ":" + str(cur_booking["flt_num"])
        booking_dict[booking_key] = Booking(**cur_booking)
    return booking_dict
