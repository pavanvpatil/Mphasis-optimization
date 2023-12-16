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
from src.fetch_input.affected_inventory_id_input import get_affected_inventory_ids

# default imports
import time

affected_inventories = get_affected_inventory_ids()

print("Processing...")

# GUI interface for changing ranking scores for alternate flight path and PNR + passenger ranking
initGUI()

start_time = time.time()

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

    if len(top_alternate_paths) == 0:
        # create solution object for this inventory and append to final solution list
        current_final_solution = AffectedInventorySolution(
            affected_inventory_id=inventory_id,
            accomodated_passengers=[],
            unaccomodated_passengers=ranked_affected_passengers_doc_ids,
            default_solution=[],
            other_solutions=[],
        )

        # append to final solution list
        final_solutions.append(current_final_solution)
        continue

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
        other_solutions=[best_solutions[i][1] for i in range(1, len(best_solutions))] if len(best_solutions) > 1 else [],
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
