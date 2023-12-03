#class for schedule exel sheet

class Schedule:
    def __init__(
            self,
            ScheduleID: str,
            CarrierCode: str,
            FlightNumber: str,
            AircraftType: str,
            AircraftTailNumber: str,
            DepartureAirport: str,
            ArrivalAirport: str,
            DepartureTime: str,
            ArrivalTime: str,
            StartDate: str,
            EndDate: str,
            Status: str,
            Sunday: str,
            Monday: str,
            Tuesday: str,
            Wednesday: str,
            Thursday: str,
            Friday: str,
            Saturday: str,
            Frequency_per_week: str,
            Frequency: str,
            NoOfDepartures: str,
            DepartureDates: str

    ):
        self.ScheduleID = ScheduleID
        self.CarrierCode = CarrierCode
        self.FlightNumber = FlightNumber
        self.AircraftType = AircraftType
        self.AircraftTailNumber = AircraftTailNumber
        self.DepartureAirport = DepartureAirport
        self.ArrivalAirport = ArrivalAirport
        self.DepartureTime = DepartureTime
        self.ArrivalTime = ArrivalTime
        self.StartDate = StartDate
        self.EndDate = EndDate
        self.Status = Status
        self.Sunday = Sunday
        self.Monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday
        self.Saturday = Saturday
        self.Frequency_per_week = Frequency_per_week
        self.Frequency = Frequency
        self.NoOfDepartures = NoOfDepartures
        self.DepartureDates = DepartureDates



