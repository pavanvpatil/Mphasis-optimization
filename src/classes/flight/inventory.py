'''
This file contains the Inventory class which is used to store the inventory data
'''


class Inventory:
    def __init__(
            self,
        inventoryid: str,
        scheduleid: str,
        flightnumber: str,
        aircrafttype: str,
        departuredate: str,
        arrivaldate: str,
        departureairport: str,
        arrivalairport: str,
        totalcapacity: str,
        totalinventory: str,
        bookedinventory: str,
        oversold: str,
        availableinventory: str,
        firstclass: str,
        businessclass: str,
        premiumeconomyclass: str,
        economyclass: str,
        fc_totalinventory: str,
        fc_bookedinventory: str,
        fc_oversold: str,
        fc_availableinventory: str,
        bc_totalinventory: str,
        bc_bookedinventory: str,
        bc_oversold: str,
        bc_availableinventory: str,
        pc_totalinventory: str,
        pc_bookedinventory: str,
        pc_oversold: str,
        pc_availableinventory: str,
        ec_totalinventory: str,
        ec_bookedinventory: str,
        ec_oversold: str,
        ec_availableinventory: str,
        fc_cd: str,
        bc_cd: str,
        pc_cd: str,
        ec_cd: str
    ):
        self.inventoryid = inventoryid
        self.scheduleid = scheduleid
        self.flightnumber = flightnumber
        self.aircrafttype = aircrafttype
        self.departuredate = departuredate
        self.arrivaldate = arrivaldate
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
