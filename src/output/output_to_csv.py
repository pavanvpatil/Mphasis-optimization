import os
import csv
from dotenv import load_dotenv
from src.classes.output.affected_inventory_sol import AffectedInventorySolution
from src.classes.flight.inventory import Inventory

load_dotenv()

output_file_path = os.getenv("OUTPUT_FILE_PATH")


def get_inventory_details(inventory_list: list[Inventory]) -> list[dict]:
    """
    Get the inventory details from the inventory list

    :param inventory_list: list of Inventory objects
    :type inventory_list: list[Inventory]
    :return: list of inventory details
    :rtype: list[dict]
    """

    inventory_details = []
    for inventory in inventory_list:
        inventory_details.append(
            {
                "Inventory_ID": inventory.inventoryid,
                "Carrier_Code": inventory.carriercode,
                "Flight_Number": inventory.flightnumber,
                "Arrival_Date_Time": inventory.arrivaldatetime,
                "Departure_Date_Time": inventory.departuredatetime,
                "Departure_Airport": inventory.departureairport,
                "Arrival_Airport": inventory.arrivalairport,
            }
        )

    return inventory_details


def output_to_csv(final_solutions: list[AffectedInventorySolution]) -> None:
    """
    Output the final solutions in a CSV file

    :param final_solutions: list of AffectedInventorySolution objects
    :return: None
    """

    fields = [
        "Affected_Inventory_ID",
        "Accomodated_Passengers_List",
        "Exception_Passengers_List",
        "Percentage_of_Passengers_Accomodated",
        "Default_Path_Solution",
        "Other_Path_Solutions",
    ]

    with open(output_file_path, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

        rows = []
        for solution in final_solutions:
            row = []
            row.append(solution.affected_inventory_id)
            row.append(solution.accomodated_passengers)
            row.append(solution.unaccomodated_passengers)
            row.append(
                str(
                    float(len(solution.accomodated_passengers))
                    / float(
                        len(solution.accomodated_passengers)
                        + len(solution.unaccomodated_passengers)
                    )
                    * 100
                )
                + "%"
            )
            row.append(get_inventory_details(solution.default_solution))
            row.append(
                [
                    get_inventory_details(other_solution)
                    for other_solution in solution.other_solutions
                ]
            )
            rows.append(row)

        csvwriter.writerows(rows)
