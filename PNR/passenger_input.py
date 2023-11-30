import os
from pandas import read_csv
from dotenv import load_dotenv
from passenger import Passenger

load_dotenv()
pnr_passenger_file_path = os.getenv("PNR_PASSENGER_FILE_PATH")

pnr_passenger_df = read_csv(pnr_passenger_file_path)

passenger_dict = {}

for index, row in pnr_passenger_df.iterrows():
    cur_passenger = pnr_passenger_df.iloc[index].to_dict()
    cur_passenger = {k.lower(): v for k, v in cur_passenger.items()}
    passenger_dict[cur_passenger["doc_id"]] = Passenger(**cur_passenger)


for k, v in passenger_dict.items():
    print(f"{k}: {v}")
    print()
    print()

print(len(passenger_dict))
