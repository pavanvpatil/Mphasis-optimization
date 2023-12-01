class Inventory:
    def __init__(
                self,
                InventoryId: str,
                ScheduleId: str,
                FlightNumber: str,
                AircraftType: str,
                DepartureDate: str,
                ArrivalDate: str,
                DepartureAirport: str,
                ArrivalAirport: str,
                TotalCapacity: str,
                TotalInventory: str,
                BookedInventory: str,
                Oversold: str,
                AvailableInventory: str,
                FirstClass: str,
                BusinessClass: str,
                PremiumEconomyClass: str,
                EconomyClass: str,
                FC_TotalInventory: str,
                FC_BookedInventory: str,
                FC_Oversold: str,
                FC_AvailableInventory: str,
                BC_TotalInventory: str,
                BC_BookedInventory: str,
                BC_Oversold: str,
                BC_AvailableInventory: str,
                PC_TotalInventory: str,
                PC_BookedInventory: str,
                PC_Oversold: str,
                PC_AvailableInventory: str,
                EC_TotalInventory: str,
                EC_BookedInventory: str,
                EC_Oversold: str,
                EC_AvailableInventory: str,
                FC_CD: str,
                BC_CD: str,
                PC_CD: str,
                EC_CD: str
                ):
        self.InventoryId = InventoryId
        self.ScheduleId = ScheduleId
        self.FlightNumber = FlightNumber
        self.AircraftType = AircraftType
        self.DepartureDate = DepartureDate
        self.ArrivalDate = ArrivalDate
        self.DepartureAirport = DepartureAirport
        self.ArrivalAirport = ArrivalAirport
        self.TotalCapacity = TotalCapacity
        self.TotalInventory = TotalInventory
        self.BookedInventory = BookedInventory
        self.Oversold = Oversold
        self.AvailableInventory = AvailableInventory
        self.FirstClass = FirstClass
        self.BusinessClass = BusinessClass
        self.PremiumEconomyClass = PremiumEconomyClass
        self.EconomyClass = EconomyClass
        self.FC_TotalInventory = FC_TotalInventory
        self.FC_BookedInventory = FC_BookedInventory
        self.FC_Oversold = FC_Oversold
        self.FC_AvailableInventory = FC_AvailableInventory
        self.BC_TotalInventory = BC_TotalInventory
        self.BC_BookedInventory = BC_BookedInventory
        self.BC_Oversold = BC_Oversold
        self.BC_AvailableInventory = BC_AvailableInventory
        self.PC_TotalInventory = PC_TotalInventory
        self.PC_BookedInventory = PC_BookedInventory
        self.PC_Oversold = PC_Oversold
        self.PC_AvailableInventory = PC_AvailableInventory
        self.EC_TotalInventory = EC_TotalInventory
        self.EC_BookedInventory = EC_BookedInventory
        self.EC_Oversold = EC_Oversold
        self.EC_AvailableInventory = EC_AvailableInventory
        self.FC_CD = FC_CD
        self.BC_CD = BC_CD
        self.PC_CD = PC_CD
        self.EC_CD = EC_CD