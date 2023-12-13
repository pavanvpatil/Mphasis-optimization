from src.rank_pnrs import get_affected_pnrs, get_affected_bookings, get_affected_passengers, get_ranked_affected_passenger_doc_ids

from src.top_alternate_path_search_dfs.dfs import init_dfs

# print(get_ranked_affected_passenger_doc_ids('INV-ZZ-6852033'))

print(init_dfs('INV-ZZ-6852033'))
