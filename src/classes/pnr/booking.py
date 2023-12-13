'''
This file contains the class for PNR booking data.
'''


class Booking:
    def __init__(
        self,
        recloc: str,
        creation_dtz: str,
        dep_key: str,
        action_cd: str,
        cos_cd: str,
        seg_seq: str,
        seg_total: str,
        pax_cnt: str,
        carrier_cd: str,
        flt_num: str,
        orig_cd: str,
        dest_cd: str,
        dep_dt: str,
        dep_dtml: str,
        arr_dtml: str,
        dep_dtmz: str,
        arr_dtmz: str,
    ) -> None:
        self.recloc: str = recloc
        self.creation_dtz: str = creation_dtz
        self.dep_key: str = dep_key
        self.action_cd: str = action_cd
        self.cos_cd: str = cos_cd
        self.seg_seq: str = seg_seq
        self.seg_total: str= seg_total
        self.pax_cnt: str = pax_cnt
        self.carrier_cd: str = carrier_cd
        self.flt_num: str = flt_num
        self.orig_cd: str = orig_cd
        self.dest_cd: str = dest_cd
        self.dep_dt: str = dep_dt
        self.dep_dtml: str = dep_dtml
        self.arr_dtml: str = arr_dtml
        self.dep_dtmz: str = dep_dtmz
        self.arr_dtmz: str = arr_dtmz

    def __repr__(self) -> str:
        return f"Booking({self.__dict__})"
