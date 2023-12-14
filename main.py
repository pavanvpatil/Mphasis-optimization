from src.passenger_accomodation.passenger_accomodation import accomodate_passengers
from src.rank_pnrs import get_ranked_affected_passenger_doc_ids
from src.rank_affected_inventory import get_rank_affected_inventories
from src.top_alternate_path_search_dfs.dfs import init_dfs
from src import inventory_dict

import time

start = time.time()

affected_inventories = [
    'INV-ZZ-3217115'
]

for inventory_id in affected_inventories:
    inventory_dict[inventory_id].is_affected = True

ranked_affected_inventories = get_rank_affected_inventories(
    affected_inventory_ids=affected_inventories
)

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
    for x in op:
        print(len(ranked_affected_passengers_doc_ids))
        print(len(x[0]))
        print(x)
        print()
        print()

end = time.time()

print(end - start)
