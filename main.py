from src.top_alternate_path_search_dfs.dfs import init_dfs

from src.rank_affected_inventory import get_rank_affected_inventories
from src.passenger_accomodation.passenger_accomodation import accomodate_passengers

affected_inventories = [
    'INV-ZZ-6852033'
]

ranked_affected_inventories = get_rank_affected_inventories(
    affected_inventory_ids=affected_inventories
)

for inventory_id in ranked_affected_inventories:
    top_alternate_paths = init_dfs(inventory_id)
    op = accomodate_passengers(
        affected_inventory_id=inventory_id,
        top_alternate_paths=top_alternate_paths
    )
    print(op)
