'''
This file contains the class for Schedule
'''


class Schedule:
    def __init__(
            self,
            scheduleid: str,
            carriercode: str,
            flightnumber: str,
            aircrafttype: str,
            aircrafttailnumber: str,
            departureairport: str,
            arrivalairport: str,
            departuretime: str,
            arrivaltime: str,
            startdate: str,
            enddate: str,
            status: str,
            sunday: str,
            monday: str,
            tuesday: str,
            wednesday: str,
            thursday: str,
            friday: str,
            saturday: str,
            frequency_per_week: str,
            frequency: str,
            noofdepartures: str,
            departuredates: str

    ):
        self.scheduleid = scheduleid
        self.carriercode = carriercode
        self.flightnumber = flightnumber
        self.aircrafttype = aircrafttype
        self.aircrafttailnumber = aircrafttailnumber
        self.departureairport = departureairport
        self.arrivalairport = arrivalairport
        self.departuretime = departuretime
        self.arrivaltime = arrivaltime
        self.startdate = startdate
        self.enddate = enddate
        self.status = status
        self.sunday = sunday
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.frequency_per_week = frequency_per_week
        self.frequency = frequency
        self.noofdepartures = noofdepartures
        self.departuredates = departuredates

    def __repr__(self) -> str:
        return f"Schedule({self.__dict__})"
