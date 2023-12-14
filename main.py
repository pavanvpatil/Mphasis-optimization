# local imports
from src.passenger_accomodation.passenger_accomodation import accomodate_passengers
from src.rank_pnrs import get_ranked_affected_passenger_doc_ids
from src.rank_affected_inventory import get_rank_affected_inventories
from src.top_alternate_path_search_dfs.dfs import init_dfs
from src import inventory_dict
from src.gui.gui import initGUI
from src.gui.gui import pnr_ranking_values_obj
from src.gui.gui import flight_ranking_values_obj

# default imports
import time

# GUI interface for changing ranking scores for alternate flight path and PNR + passenger ranking
initGUI()

print(pnr_ranking_values_obj)
print(flight_ranking_values_obj)

start_time = time.time()

affected_inventories = [
    'INV-ZZ-2774494',
    'INV-ZZ-8029879',
    'INV-ZZ-6852033',
    'INV-ZZ-7065859',
    'INV-ZZ-1595392',
    'INV-ZZ-2946425',
    'INV-ZZ-4457881',
    'INV-ZZ-4268320',
    'INV-ZZ-8140596',
    'INV-ZZ-1617071',
    'INV-ZZ-4593004',
    'INV-ZZ-5954450',
    'INV-ZZ-5984671',
    'INV-ZZ-1992356',
    'INV-ZZ-5501386',
    'INV-ZZ-2354255',
    'INV-ZZ-4023564',
    'INV-ZZ-1796152',
    'INV-ZZ-9027725',
    'INV-ZZ-2014595',
    'INV-ZZ-2141857',
    'INV-ZZ-5971833',
    'INV-ZZ-3384608',
    'INV-ZZ-1676817',
    'INV-ZZ-8324457',
    'INV-ZZ-2400044',
]

for inventory_id in affected_inventories:
    inventory_dict[inventory_id].is_affected = True

ranked_affected_inventories = get_rank_affected_inventories(
    affected_inventory_ids=affected_inventories
)

print('------------------')

for inventory_id in ranked_affected_inventories:

    top_alternate_paths = init_dfs(inventory_id)

    ranked_affected_passengers_doc_ids = get_ranked_affected_passenger_doc_ids(
        inventory_id=inventory_id
    )

    op = accomodate_passengers(
        ranked_affected_passengers_doc_ids=ranked_affected_passengers_doc_ids,
        affected_inventory_id=inventory_id,
        top_alternate_paths=top_alternate_paths
    )

    print(inventory_id)
    print(len(op[0][0]))
    print(len(ranked_affected_passengers_doc_ids))
    print('------------------')

end_time = time.time()

print('Ended in ', end_time - start_time, ' seconds')
