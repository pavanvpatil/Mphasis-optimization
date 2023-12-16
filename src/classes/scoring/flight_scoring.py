'''
This file has the class to store Flight scores config
'''


class FlightScoringConfig:
    def __init__(
        self,
        distance_score: float,
        arr_time_multiplier: float,
        dep_time_multiplier: float,
        equipment_multiplier: float,
        stop_over_score: float,
        max_downline_flights: int,
        no_of_top_flights: int,
        max_connection_time_hrs: int,
        min_connection_time_hrs: int
    ):
        self.distance_score = distance_score
        self.arr_time_multiplier = arr_time_multiplier
        self.dep_time_multiplier = dep_time_multiplier
        self.equipment_multiplier = equipment_multiplier
        self.stop_over_score = stop_over_score
        self.max_dowline_flights = max_downline_flights
        self.no_of_top_flights = no_of_top_flights
        self.max_connection_time_hrs = max_connection_time_hrs
        self.min_connection_time_hrs = min_connection_time_hrs

    def __repr__(self) -> str:
        return f'''
        distance_score: {self.distance_score}
        arr_time_multiplier: {self.arr_time_multiplier}
        dep_time_multiplier: {self.dep_time_multiplier}
        equipment_multiplier: {self.equipment_multiplier}
        stop_over_score: {self.stop_over_score}
        max_downline_flights: {self.max_dowline_flights}
        no_of_top_flights: {self.no_of_top_flights}
        min_connection_time_hrs: {self.min_connection_time_hrs}
        max_connection_time_hrs: {self.max_connection_time_hrs}
        '''
