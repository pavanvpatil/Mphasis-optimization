'''
This file has the class to store Flight scores config
'''


class FlightScoringConfig:
    def __init__(self,
                 distance_score: float,
                 arr_time_multiplier: float,
                 dep_time_multiplier: float,
                 equipment_multiplier: float,
                 stop_over_score: float):
        self.distance_score = distance_score
        self.arr_time_multiplier = arr_time_multiplier
        self.dep_time_multiplier = dep_time_multiplier
        self.equipment_multiplier = equipment_multiplier
        self.stop_over_score = stop_over_score

    def __repr__(self) -> str:
        return f'''
        distance_score: {self.distance_score}
        arr_time_multiplier: {self.arr_time_multiplier}
        dep_time_multiplier: {self.dep_time_multiplier}
        equipment_multiplier: {self.equipment_multiplier}
        stop_over_score: {self.stop_over_score}
        '''
