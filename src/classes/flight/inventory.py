'''
This file contains the Inventory class which is used to store the inventory data
'''


class Inventory:
    def __init__(
            self,
        inventoryid: str,
        scheduleid: str,
        carriercode: str,
        dep_key: str,
        flightnumber: str,
        aircrafttype: str,
        departuredate: str,
        departuredatetime: str,
        arrivaldatetime: str,
        departureairport: str,
        arrivalairport: str,
        totalcapacity: int,
        totalinventory: int,
        bookedinventory: int,
        oversold: int,
        availableinventory: int,
        firstclass: int,
        businessclass: int,
        premiumeconomyclass: int,
        economyclass: int,
        fc_totalinventory: int,
        fc_bookedinventory: int,
        fc_oversold: int,
        fc_availableinventory: int,
        bc_totalinventory: int,
        bc_bookedinventory: int,
        bc_oversold: int,
        bc_availableinventory: int,
        pc_totalinventory: int,
        pc_bookedinventory: int,
        pc_oversold: int,
        pc_availableinventory: int,
        ec_totalinventory: int,
        ec_bookedinventory: int,
        ec_oversold: int,
        ec_availableinventory: int,
        fc_cd: dict[str, int],
        bc_cd: dict[str, int],
        pc_cd: dict[str, int],
        ec_cd: dict[str, int]
    ):
        self.is_affected = False
        self.inventoryid = inventoryid
        self.scheduleid = scheduleid
        self.carriercode = carriercode
        self.dep_key = dep_key
        self.flightnumber = flightnumber
        self.aircrafttype = aircrafttype
        self.departuredate = departuredate
        self.departuredatetime = departuredatetime
        self.arrivaldatetime = arrivaldatetime
        self.departureairport = departureairport
        self.arrivalairport = arrivalairport
        self.totalcapacity = totalcapacity
        self.totalinventory = totalinventory
        self.bookedinventory = bookedinventory
        self.oversold = oversold
        self.availableinventory = availableinventory
        self.firstclass = firstclass
        self.businessclass = businessclass
        self.premiumeconomyclass = premiumeconomyclass
        self.economyclass = economyclass
        self.fc_totalinventory = fc_totalinventory
        self.fc_bookedinventory = fc_bookedinventory
        self.fc_oversold = fc_oversold
        self.fc_availableinventory = fc_availableinventory
        self.bc_totalinventory = bc_totalinventory
        self.bc_bookedinventory = bc_bookedinventory
        self.bc_oversold = bc_oversold
        self.bc_availableinventory = bc_availableinventory
        self.pc_totalinventory = pc_totalinventory
        self.pc_bookedinventory = pc_bookedinventory
        self.pc_oversold = pc_oversold
        self.pc_availableinventory = pc_availableinventory
        self.ec_totalinventory = ec_totalinventory
        self.ec_bookedinventory = ec_bookedinventory
        self.ec_oversold = ec_oversold
        self.ec_availableinventory = ec_availableinventory
        self.fc_cd = fc_cd
        self.bc_cd = bc_cd
        self.pc_cd = pc_cd
        self.ec_cd = ec_cd

    def __repr__(self) -> str:
        return f"Inventory({self.__dict__})"
