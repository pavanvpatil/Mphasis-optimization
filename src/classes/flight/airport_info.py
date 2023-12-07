'''
This class is used to store information about an airport.
'''

class AirportInfo:
    def __init__(
            self, airport_code: str,
            city_name: str,
            country_code: str,
            airport_name: str,
            lat: float,
            long: float):
        self.airport_code = airport_code
        self.city_name = city_name
        self.airport_name = airport_name
        self.country_code = country_code
        self.lat = lat
        self.long = long

    def __repr__(self) -> str:
        return f"AirportInfo({self.__dict__})"