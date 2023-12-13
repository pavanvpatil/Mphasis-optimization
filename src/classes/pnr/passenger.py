'''
This file contains the class for PNR passenger data.
'''


class Passenger:

    def __init__(
        self,
        doc_id: str,
        recloc: str,
        creation_dtz: str,
        customer_id: str,
        first_name: str,
        last_name: str,
        nationality: str,
        dob: str,
        contact_ph_num: str,
        contact_email: str,
        doc_type: str,
        special_name_cd1: str,
        special_name_cd2: str,
        ssr_code_cd1: str,
        ff_num: str,
        tierlevel: str
    ) -> None:
        self.doc_id: str = doc_id
        self.recloc: str = recloc
        self.creation_dtz: str = creation_dtz
        self.customer_id:str = customer_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.nationality: str = nationality
        self.dob:str = dob
        self.contact_ph_num: str = contact_ph_num
        self.contact_email: str = contact_email
        self.doc_type: str = doc_type
        self.special_name_cd1: str = special_name_cd1
        self.special_name_cd2: str = special_name_cd2
        self.ssr_code_cd1: str = ssr_code_cd1
        self.ff_num: str = ff_num
        self.tierlevel: str = tierlevel

    def __repr__(self) -> str:
        return f"Passenger({self.__dict__})"
