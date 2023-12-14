import PySimpleGUI as psg


pnr_ranking_vals = {'loyalties_pplatinum': 2000, 'loyalties_platinum': 1800, 'loyalties_gold': 1600, 'loyalties_silver': 1500, 'ssr_score': 200, 'pax_cnt_score': 50, 'first_class_score': 1700, 'business_class_score': 2000, 'eco_class_score': 1500}

def initGUI():
    '''
    call this function to initialise the GUI to change pnr_ranking_vals
    atribute:None
    rtype:None
    '''
    layout = []

    layout.append([psg.Text("PNR Ranking Scoring", justification='centre')])

    layout.append([psg.Checkbox("Premium Platinum Loyalties", key="loyalties_pplatinum", default=True,
                                enable_events=True, size=(30, 2)),
                   psg.Input("2000", key="loyalties_pplatinum_score", enable_events=True)])
    layout.append([psg.Checkbox("Platinum Loyalties        ", key="loyalties_platinum", default=True,
                                enable_events=True, size=(30, 1)),
                   psg.Input("1800", key="loyalties_platinum_score", enable_events=True)])
    layout.append([psg.Checkbox("Gold Loyalties            ", key="loyalties_gold", default=True, enable_events=True,
                                size=(30, 1)), psg.Input("1600", key="loyalties_gold_score", enable_events=True)])
    layout.append([psg.Checkbox("Silver Loyalties          ", key="loyalties_silver", default=True, enable_events=True,
                                size=(30, 1)), psg.Input("1500", key="loyalties_silver_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("SSR                       ", key="ssr", default=True, enable_events=True, size=(30, 1)),
         psg.Input("200", key="ssr_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("Passenger Count           ", key="pax_cnt", default=True, enable_events=True, size=(30, 1)),
         psg.Input("50", key="pax_cnt_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("First Class               ", key="first_class", default=True, enable_events=True, size=(30, 1)),
         psg.Input("1700", key="first_class_score", enable_events=True)])
    layout.append([psg.Checkbox("Business Class            ", key="business_class", default=True, enable_events=True,
                                size=(30, 1)), psg.Input("2000", key="business_class_score", enable_events=True)])
    layout.append(
        [psg.Checkbox("Economy Class             ", key="eco_class", default=True, enable_events=True, size=(30, 1)),
         psg.Input("1500", key="eco_class_score", enable_events=True)])
    layout.append([psg.Button("SAVE", size=(1000, 2))])

    window = psg.Window("PNR Scoring", layout, size=(1000, 800))

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "SAVE":
            if values["loyalties_pplatinum"]:
                pnr_ranking_vals["loyalties_pplatinum"] = int(values["loyalties_pplatinum_score"])
            else:
                pnr_ranking_vals["loyalties_pplatinum"] = 0
            if values["loyalties_platinum"]:
                pnr_ranking_vals["loyalties_platinum"] = int(values["loyalties_platinum_score"])
            else:
                pnr_ranking_vals["loyalties_platinum"] = 0
            if values["loyalties_gold"]:
                pnr_ranking_vals["loyalties_gold"] = int(values["loyalties_gold_score"])
            else:
                pnr_ranking_vals["loyalties_gold"] = 0
            if values["loyalties_silver"]:
                pnr_ranking_vals["loyalties_silver"] = int(values["loyalties_silver_score"])
            else:
                pnr_ranking_vals["loyalties_silver"] = 0
            if values["ssr"]:
                pnr_ranking_vals["ssr_score"] = int(values["ssr_score"])
            else:
                pnr_ranking_vals["ssr_score"] = 0
            if values["pax_cnt"]:
                pnr_ranking_vals["pax_cnt_score"] = int(values["pax_cnt_score"])
            else:
                pnr_ranking_vals["pax_cnt_score"] = 0
            if values["first_class"]:
                pnr_ranking_vals["first_class_score"] = int(values["first_class_score"])
            else:
                pnr_ranking_vals["first_class_score"] = 0
            if values["business_class"]:
                pnr_ranking_vals["business_class_score"] = int(values["business_class_score"])
            else:
                pnr_ranking_vals["business_class_score"] = 0
            if values["eco_class"]:
                pnr_ranking_vals["eco_class_score"] = int(values["eco_class_score"])
            else:
                pnr_ranking_vals["eco_class_score"] = 0

            break





