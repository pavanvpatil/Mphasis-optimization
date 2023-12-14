import PySimpleGUI as psg
from src.classes.scoring.pnr_scoring import PNRScoringConfig
from src.classes.scoring.flight_scoring import FlightScoringConfig

pnr_ranking_values_dict = {'loyalties_pplatinum': 2000, 'loyalties_platinum': 1800, 'loyalties_gold': 1600,
                           'loyalties_silver': 1500, 'ssr_score': 200, 'pax_cnt_score': 50, 'first_class_score': 1700,
                           'business_class_score': 2000, 'eco_class_score': 1500}
flight_ranking_values_dict = {'distance_score': 100, 'arr_time_multiplier': 70, 'dep_time_multiplier': 70,
                              'equipment_multiplier': 50, 'stop_over_score': -20}


# pnr_ranking_vals = PNR_scoring(**pnr_ranking_values_dict)


def get_pnr_ranking_values() -> PNRScoringConfig:
    '''
    function to get pnr ranking values
    attribute:None
    rtype:PNRSCoringConfig object
    '''
    return PNRScoringConfig(**pnr_ranking_values_dict)


def get_flight_scoring_values() -> FlightScoringConfig:
    '''
    function to get flight ranking values
    attribute:None
    rtype:FlightSCoringConfig object
        '''
    return FlightScoringConfig(**flight_ranking_values_dict)


def initGUI():
    '''
    call this function to initialise the GUI to change pnr_ranking_values_dict
    atribute:None
    rtype:None
    '''
    layout = []

    layout.append(
        [psg.Text("PNR Ranking Scoring", size=(50, 1))])

    layout.append([psg.Checkbox("Premium Platinum Loyalties", key="loyalties_pplatinum", default=True,
                                enable_events=True, size=(30, 2)),
                   psg.Input("2000", key="loyalties_pplatinum_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("Platinum Loyalties", key="loyalties_platinum", default=True, enable_events=True, size=(30, 1)),
         psg.Input("1800", key="loyalties_platinum_score", enable_events=True)])
    layout.append([psg.Checkbox("Gold Loyalties", key="loyalties_gold", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("1600", key="loyalties_gold_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("Silver Loyalties", key="loyalties_silver", default=True, enable_events=True, size=(30, 1)),
         psg.Input("1500", key="loyalties_silver_score", enable_events=True)])
    layout.append([psg.Checkbox("SSR", key="ssr", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("200", key="ssr_score", enable_events=True)])
    layout.append([psg.Checkbox("Passenger Count", key="pax_cnt", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("50", key="pax_cnt_score", enable_events=True)])
    layout.append([psg.Checkbox("First Class", key="first_class", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("1700", key="first_class_score", enable_events=True)])
    layout.append([psg.Checkbox("Business Class", key="business_class", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("2000", key="business_class_score", enable_events=True)])
    layout.append([psg.Checkbox("Economy Class", key="eco_class", default=True, enable_events=True, size=(30, 1)),
                   psg.Input("1500", key="eco_class_score", enable_events=True)])
    layout.append([psg.Text("Flight Scoring")])
    layout.append([psg.Checkbox("Distance Score Multiplier",default=True,key='distance_score_check', size=(30, 1)),
                   psg.Input("100", key='distance_score', enable_events=True)])
    layout.append([psg.Checkbox("Arrival Time Score Multiplier",default=True,key='arr_time_multiplier_check', size=(30, 1)), psg.Input("70", key='arr_time_multiplier')])
    layout.append(
        [psg.Checkbox("Departure Time Score Multiplier",default=True,key='dep_time_multiplier_check', size=(30, 1)), psg.Input("70", key='dep_time_multiplier')])
    layout.append([psg.Checkbox("Equipment Score Multiplier",default=True, key='equipment_score_check', size=(30, 1)), psg.Input("50", key='equipment_multiplier')])
    layout.append([psg.Checkbox("Stop Over Score",default=True,key='stop_over_score_check', size=(30, 1)), psg.Input("-20", key='stop_over_score')])

    layout.append([psg.Button("SAVE", key='save', size=(100, 2))])

    window = psg.Window("PNR Scoring", layout, size=(1000, 800))

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "save":
            if values["loyalties_pplatinum"]:
                pnr_ranking_values_dict["loyalties_pplatinum"] = float(values["loyalties_pplatinum_score"])
            else:
                pnr_ranking_values_dict["loyalties_pplatinum"] = 0
            if values["loyalties_platinum"]:
                pnr_ranking_values_dict["loyalties_platinum"] = float(values["loyalties_platinum_score"])
            else:
                pnr_ranking_values_dict["loyalties_platinum"] = 0
            if values["loyalties_gold"]:
                pnr_ranking_values_dict["loyalties_gold"] = float(values["loyalties_gold_score"])
            else:
                pnr_ranking_values_dict["loyalties_gold"] = 0
            if values["loyalties_silver"]:
                pnr_ranking_values_dict["loyalties_silver"] = float(values["loyalties_silver_score"])
            else:
                pnr_ranking_values_dict["loyalties_silver"] = 0
            if values["ssr"]:
                pnr_ranking_values_dict["ssr_score"] = float(values["ssr_score"])
            else:
                pnr_ranking_values_dict["ssr_score"] = 0
            if values["pax_cnt"]:
                pnr_ranking_values_dict["pax_cnt_score"] = float(values["pax_cnt_score"])
            else:
                pnr_ranking_values_dict["pax_cnt_score"] = 0
            if values["first_class"]:
                pnr_ranking_values_dict["first_class_score"] = float(values["first_class_score"])
            else:
                pnr_ranking_values_dict["first_class_score"] = 0
            if values["business_class"]:
                pnr_ranking_values_dict["business_class_score"] = float(values["business_class_score"])
            else:
                pnr_ranking_values_dict["business_class_score"] = 0
            if values["eco_class"]:
                pnr_ranking_values_dict["eco_class_score"] = float(values["eco_class_score"])
            else:
                pnr_ranking_values_dict["eco_class_score"] = 0

            if values['distance_score_check']:
                flight_ranking_values_dict['distance_score'] = float(values['distance_score'])
            else:
                flight_ranking_values_dict['distance_score'] = 0
            if values['arr_time_multiplier_check']:
                flight_ranking_values_dict['arr_time_multiplier'] = float(values['arr_time_multiplier'])
            else:
                flight_ranking_values_dict['arr_time_multiplier'] = 0
            if values['dep_time_multiplier_check']:
                flight_ranking_values_dict['dep_time_multiplier'] = float(values['dep_time_multiplier'])
            else:
                flight_ranking_values_dict['dep_time_multiplier'] = 0
            if values['equipment_score_check']:
                flight_ranking_values_dict['equipment_multiplier'] = float(values['equipment_multiplier'])
            else:
                flight_ranking_values_dict['equipment_multiplier'] = 0
            if values['stop_over_score_check']:
                flight_ranking_values_dict['stop_over_score'] = float(values['stop_over_score'])
            flight_ranking_values_dict['stop_over_score'] = 0

            window.close()
            break
if __name__ == "__main__":
    initGUI()



