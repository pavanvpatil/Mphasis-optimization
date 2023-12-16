import os
from src import inventory_dict
from dotenv import load_dotenv
from pandas import read_csv

load_dotenv()

affected_inventory_file_path = os.getenv("AFFECTED_INVENTORY_FILE_PATH")


def get_affected_inventory_ids(
):
    '''This method returns a list of affected inventory ids

    :param None
    :return: set of affected inventory ids
    :rtype: set[str]
    '''

    try:
        affected_inv_df = read_csv(affected_inventory_file_path)
    except FileNotFoundError:
        print("Affected inventory file not found")
        exit(1)

    affected_inv = set()
    for index, row in affected_inv_df.iterrows():
        cur_row = affected_inv_df.iloc[index].to_dict()
        cur_row = {k.lower(): v for k, v in cur_row.items()}
        affected_inv.add(cur_row["inventory_id"])
    return affected_inv
