# local imports
from src.passenger_accomodation.passenger_accomodation import accomodate_passengers
from src.rank_pnrs import get_ranked_affected_passenger_doc_ids
from src.rank_affected_inventory import get_rank_affected_inventories
from src.top_alternate_path_search_dfs.dfs import init_dfs
from src import inventory_dict
from src.classes.output.affected_inventory_sol import AffectedInventorySolution
from src.output.output_to_csv import output_to_csv
from src.gui.gui import initGUI
from src.mail_service.mailing import driver_send_mail

# default imports
import time

# GUI interface for changing ranking scores for alternate flight path and PNR + passenger ranking
initGUI()

print("Processing...")
start_time = time.time()

# affected inventory ids
affected_inventories = [
    "INV-ZZ-2774494",
    "INV-ZZ-8029879",
    "INV-ZZ-6852033",
    "INV-ZZ-7065859",
    "INV-ZZ-1595392",
    "INV-ZZ-2946425",
    "INV-ZZ-4457881",
    "INV-ZZ-4268320",
    "INV-ZZ-8140596",
    "INV-ZZ-1617071",
    "INV-ZZ-4593004",
    "INV-ZZ-5954450",
    "INV-ZZ-5984671",
    "INV-ZZ-1992356",
    "INV-ZZ-5501386",
    "INV-ZZ-2354255",
    "INV-ZZ-4023564",
    "INV-ZZ-1796152",
    "INV-ZZ-9027725",
    "INV-ZZ-2014595",
    "INV-ZZ-2141857",
    "INV-ZZ-5971833",
    "INV-ZZ-3384608",
    "INV-ZZ-1676817",
    "INV-ZZ-8324457",
    "INV-ZZ-2400044",
]

for inventory_id in affected_inventories:
    inventory_dict[inventory_id].is_affected = True

ranked_affected_inventories = get_rank_affected_inventories(
    affected_inventory_ids=affected_inventories
)

final_solutions: list[AffectedInventorySolution] = []

for inventory_id in ranked_affected_inventories:
    # initialize dfs for this inventory and get top alternate paths
    top_alternate_paths = init_dfs(inventory_id)

    # get ranked affected passengers for this inventory sorted according to their passenger score
    ranked_affected_passengers_doc_ids = get_ranked_affected_passenger_doc_ids(
        inventory_id=inventory_id
    )

    # solution list after accomodating passengers for this inventory in each of the top 3 alternate paths
    best_solutions = accomodate_passengers(
        ranked_affected_passengers_doc_ids=ranked_affected_passengers_doc_ids,
        affected_inventory_id=inventory_id,
        top_alternate_paths=top_alternate_paths,
    )

    accomodate_passengers_set = set(best_solutions[0][0])
    unaccomodated_passengers = []
    for passenger_doc_id in ranked_affected_passengers_doc_ids:
        if passenger_doc_id not in accomodate_passengers_set:
            unaccomodated_passengers.append(passenger_doc_id)

    # create solution object for this inventory and append to final solution list
    current_final_solution = AffectedInventorySolution(
        affected_inventory_id=inventory_id,
        accomodated_passengers=best_solutions[0][0],
        unaccomodated_passengers=unaccomodated_passengers,
        default_solution=best_solutions[0][1],
        other_solutions=[best_solutions[i][1] for i in range(1, len(best_solutions))],
    )

    # append to final solution list
    final_solutions.append(current_final_solution)

end_time = time.time()
print("Process ended in ", end_time - start_time, " seconds")

# output to csv
print("Creating output csv file in final_solution folder")
output_to_csv(final_solutions=final_solutions)
print("Created output csv file in final_solution folder")

# send mail to passengers
print("Sending mail to passengers")
driver_send_mail(final_solutions=final_solutions)
print("Sent mail to passengers")