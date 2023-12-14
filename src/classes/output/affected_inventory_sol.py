from src.classes.flight.inventory import Inventory


class AffectedInventorySolution:

    def __init__(
        self,
        affected_inventory_id: str,
        accomodated_passengers: list[str],
        unaccomodated_passengers: list[str],
        default_solution: list[Inventory],
        other_solutions: list[list[Inventory]]
    ):
        self.affected_inventory_id = affected_inventory_id
        self.accomodated_passengers = accomodated_passengers
        self.unaccomodated_passengers = unaccomodated_passengers
        self.default_solution = default_solution
        self.other_solutions = other_solutions

    def __repr__(self) -> str:
        return f"AffectedInventorySolution({self.affected_inventory_id})"
