import os
import csv
from dotenv import load_dotenv
from src.classes.output.affected_inventory_sol import AffectedInventorySolution

load_dotenv()

output_file_path = os.getenv("OUTPUT_FILE_PATH")


def output_to_csv(final_solutions: list[AffectedInventorySolution]):
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
            rows.append(row)

        csvwriter.writerows(rows)
