'''
this files has the class to store PNR scoring config
'''

class PNRScoringConfig:
    def __init__(self,loyalties_pplatinum: float,
                loyalties_platinum: float,
                loyalties_gold: float,
                loyalties_silver: float,
                ssr_score: float,
                pax_cnt_score: float,
                first_class_score : float,
                business_class_score: float,
                eco_class_score: float):

        self.loyalties_pplatinum: float = loyalties_pplatinum
        self.loyalties_platinum: float = loyalties_platinum
        self.loyalties_gold : float = loyalties_gold
        self.loyalties_silver: float = loyalties_silver
        self.ssr_score: float = ssr_score
        self.pax_cnt_score: float = pax_cnt_score
        self.first_class_score: float = first_class_score
        self.business_class_score: float = business_class_score
        self.eco_class_score: float = eco_class_score