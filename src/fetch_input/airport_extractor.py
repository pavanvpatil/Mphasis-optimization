import os
from pandas import read_csv
from dotenv import load_dotenv
from src.classes.flight.airport_info import AirportInfo

load_dotenv()
airport_codes_file_path = os.getenv("AIRPORT_CODES_FILE_PATH")

try:
    airport_codes_df = read_csv(airport_codes_file_path)
except FileNotFoundError:
    print("Airport codes file not found")
    exit(1)


def get_airport_city_codes() -> dict[str, str]:
    '''Returns a dictionary of airport codes to city names

    :param: None
    :return: dictionary of airport codes to city names
    :rtype: dict[str, str]
    '''

    airport_code_to_city_dict = {}
    for index, row in airport_codes_df.iterrows():
        cur_airport = airport_codes_df.iloc[index].to_dict()
        airport_code_to_city_dict[cur_airport["airport_code"]
                                  ] = cur_airport["city_name"]

    return airport_code_to_city_dict


def get_airport_info() -> dict[str, AirportInfo]:
    '''Returns a dictionary of airport codes to airport information

    :param: None
    :return: dictionary of airport codes to airport information
    :rtype: dict
    '''

    airport_info_dict = {}
    for index, row in airport_codes_df.iterrows():
        cur_airport = airport_codes_df.iloc[index].to_dict()
        airport_info_dict[cur_airport["airport_code"]
                          ] = AirportInfo(**cur_airport)

    return airport_info_dict
