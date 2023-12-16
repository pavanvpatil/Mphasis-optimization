import PySimpleGUI as psg
from src.classes.scoring.pnr_scoring import PNRScoringConfig
from src.classes.scoring.flight_scoring import FlightScoringConfig

pnr_ranking_values_obj = PNRScoringConfig(
    loyalties_pplatinum=2000,
    loyalties_platinum=1800,
    loyalties_gold=1600,
    loyalties_silver=1500,
    ssr_score=200,
    pax_cnt_score=50,
    business_class_score=2000,
    first_class_score=1800,
    premium_eco_class_score=1650,
    eco_class_score=1500,
)

flight_ranking_values_obj = FlightScoringConfig(
    distance_score=100,
    arr_time_multiplier=70,
    dep_time_multiplier=70,
    equipment_multiplier=50,
    stop_over_score=-20,
    max_downline_flights=3,
    no_of_top_flights=3,
    min_connection_time_hrs=1,
    max_connection_time_hrs=12,
)


def initGUI() -> None:
    """
    call this function to initialise the GUI to change pnr_ranking_values_obj and flight_ranking_values_obj
    :param None
    :return: None
    :rtype: None
    """
    layout = []

    layout.append(
        [
            psg.Text(
                text="PNR Ranking Scoring",
                size=(None, 1),
                justification="center",
                font=("Helvetica", 15),
                background_color="white",
                text_color="black",
                relief=psg.RELIEF_RIDGE,
            )
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Premium Platinum Loyalties",
                key="loyalties_pplatinum",
                default=True,
                enable_events=True,
                size=(30, 2),
            ),
            psg.Input("2000", key="loyalties_pplatinum_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Platinum Loyalties",
                key="loyalties_platinum",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1800", key="loyalties_platinum_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Gold Loyalties",
                key="loyalties_gold",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1600", key="loyalties_gold_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Silver Loyalties",
                key="loyalties_silver",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1500", key="loyalties_silver_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "SSR", key="ssr", default=True, enable_events=True, size=(30, 1)
            ),
            psg.Input("200", key="ssr_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Passenger Count",
                key="pax_cnt",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("50", key="pax_cnt_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Business Class",
                key="business_class",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("2000", key="business_class_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "First Class",
                key="first_class",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1800", key="first_class_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Premium Economy Class",
                key="premium_eco_class",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1650", key="premium_eco_class_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Economy Class",
                key="eco_class",
                default=True,
                enable_events=True,
                size=(30, 1),
            ),
            psg.Input("1500", key="eco_class_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Text(
                text="Flight Scoring",
                size=(None, 1),
                justification="center",
                font=("Helvetica", 15),
                background_color="white",
                text_color="black",
                relief=psg.RELIEF_RIDGE,
            )
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Distance Score Multiplier",
                default=True,
                key="distance_score_check",
                size=(30, 1),
                enable_events=True,
            ),
            psg.Input("100", key="distance_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Arrival Time Score Multiplier",
                default=True,
                key="arr_time_multiplier_check",
                size=(30, 1),
                enable_events=True,
            ),
            psg.Input("70", key="arr_time_multiplier", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Departure Time Score Multiplier",
                default=True,
                key="dep_time_multiplier_check",
                size=(30, 1),
                enable_events=True,
            ),
            psg.Input("70", key="dep_time_multiplier", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Equipment Score Multiplier",
                default=True,
                key="equipment_score_check",
                size=(30, 1),
                enable_events=True,
            ),
            psg.Input("50", key="equipment_multiplier", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Checkbox(
                "Stop Over Score",
                default=True,
                key="stop_over_score_check",
                size=(30, 1),
                enable_events=True,
            ),
            psg.Input("-20", key="stop_over_score", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Text(
                text="Mandatory Flight Configurations",
                size=(None, 1),
                justification="center",
                font=("Helvetica", 15),
                background_color="white",
                text_color="black",
                relief=psg.RELIEF_RIDGE,
            )
        ]
    )

    layout.append(
        [
            psg.Text(
                "Maximum number of dowline flights", size=(32, 1), enable_events=True
            ),
            psg.Input("3", key="max_downline_flights", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Text(
                "Number of top flights considered", size=(32, 1), enable_events=True
            ),
            psg.Input("3", key="no_of_top_flights", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Text(
                "Minimum connection time in hours", size=(32, 1), enable_events=True
            ),
            psg.Input("1", key="min_connection_time_hrs", enable_events=True),
        ]
    )

    layout.append(
        [
            psg.Text(
                "Maximum connection time in hours", size=(32, 1), enable_events=True
            ),
            psg.Input("12", key="max_connection_time_hrs", enable_events=True),
        ]
    )

    layout.append([psg.Button("SAVE", key="save", size=(None, 1), pad=10)])

    window = psg.Window(
        "Mphasis Optimization Tool",
        element_justification="center",
        layout=layout,
        resizable=True,
    )

    while True:
        event, values = window.read()
        if event == psg.WIN_CLOSED or event == "save":
            if values["loyalties_pplatinum"]:
                pnr_ranking_values_obj.loyalties_pplatinum = float(
                    values["loyalties_pplatinum_score"]
                )
            else:
                pnr_ranking_values_obj.loyalties_pplatinum = 0.0

            if values["loyalties_platinum"]:
                pnr_ranking_values_obj.loyalties_platinum = float(
                    values["loyalties_platinum_score"]
                )
            else:
                pnr_ranking_values_obj.loyalties_platinum = 0.0

            if values["loyalties_gold"]:
                pnr_ranking_values_obj.loyalties_gold = float(
                    values["loyalties_gold_score"]
                )
            else:
                pnr_ranking_values_obj.loyalties_gold = 0.0

            if values["loyalties_silver"]:
                pnr_ranking_values_obj.loyalties_silver = float(
                    values["loyalties_silver_score"]
                )
            else:
                pnr_ranking_values_obj.loyalties_silver = 0.0

            if values["ssr"]:
                pnr_ranking_values_obj.ssr_score = float(values["ssr_score"])
            else:
                pnr_ranking_values_obj.ssr_score = 0.0

            if values["pax_cnt"]:
                pnr_ranking_values_obj.pax_cnt_score = float(values["pax_cnt_score"])
            else:
                pnr_ranking_values_obj.pax_cnt_score = 0.0

            if values["first_class"]:
                pnr_ranking_values_obj.first_class_score = float(
                    values["first_class_score"]
                )
            else:
                pnr_ranking_values_obj.first_class_score = 0.0

            if values["business_class"]:
                pnr_ranking_values_obj.business_class_score = float(
                    values["business_class_score"]
                )
            else:
                pnr_ranking_values_obj.business_class_score = 0.0

            if values["premium_eco_class"]:
                pnr_ranking_values_obj.premium_eco_class_score = float(
                    values["premium_eco_class_score"]
                )
            else:
                pnr_ranking_values_obj.premium_eco_class_score = 0.0

            if values["eco_class"]:
                pnr_ranking_values_obj.eco_class_score = float(
                    values["eco_class_score"]
                )
            else:
                pnr_ranking_values_obj.eco_class_score = 0.0

            if values["distance_score_check"]:
                flight_ranking_values_obj.distance_score = float(
                    values["distance_score"]
                )
            else:
                flight_ranking_values_obj.distance_score = 0.0

            if values["arr_time_multiplier_check"]:
                flight_ranking_values_obj.arr_time_multiplier = float(
                    values["arr_time_multiplier"]
                )
            else:
                flight_ranking_values_obj.arr_time_multiplier = 0.0

            if values["dep_time_multiplier_check"]:
                flight_ranking_values_obj.dep_time_multiplier = float(
                    values["dep_time_multiplier"]
                )
            else:
                flight_ranking_values_obj.dep_time_multiplier = 0.0

            if values["equipment_score_check"]:
                flight_ranking_values_obj.equipment_multiplier = float(
                    values["equipment_multiplier"]
                )
            else:
                flight_ranking_values_obj.equipment_multiplier = 0.0

            if values["stop_over_score_check"]:
                flight_ranking_values_obj.stop_over_score = float(
                    values["stop_over_score"]
                )
            else:
                flight_ranking_values_obj.stop_over_score = 0.0

            if values["max_downline_flights"]:
                flight_ranking_values_obj.no_of_top_flights = int(
                    values["no_of_top_flights"]
                )

            if values["max_downline_flights"]:
                flight_ranking_values_obj.max_dowline_flights = int(
                    values["max_downline_flights"]
                )

            if values["min_connection_time_hrs"]:
                flight_ranking_values_obj.min_connection_time_hrs = int(
                    values["min_connection_time_hrs"]
                )

            if values["max_connection_time_hrs"]:
                flight_ranking_values_obj.max_connection_time_hrs = int(
                    values["max_connection_time_hrs"]
                )

            if (
                flight_ranking_values_obj.max_connection_time_hrs
                < flight_ranking_values_obj.min_connection_time_hrs
            ):
                psg.popup(
                    "Maximum connection time cannot be less than minimum connection time",
                    button_type=psg.POPUP_BUTTONS_OK,
                )
                continue

            if (
                flight_ranking_values_obj.max_connection_time_hrs < 0
                or flight_ranking_values_obj.min_connection_time_hrs < 0
            ):
                psg.popup("Connection time cannot be negative")
                continue

            if flight_ranking_values_obj.max_dowline_flights <= 0:
                psg.popup("Maximum downline flights must be greater than 0")
                continue

            if flight_ranking_values_obj.no_of_top_flights <= 0:
                psg.popup("Number of top flights must be greater than 0")
                continue

            if flight_ranking_values_obj.distance_score < 0:
                psg.popup("Distance score multiplier cannot be negative")
                continue

            if flight_ranking_values_obj.arr_time_multiplier < 0:
                psg.popup("Arrival time score multiplier cannot be negative")
                continue

            if flight_ranking_values_obj.dep_time_multiplier < 0:
                psg.popup("Departure time score multiplier cannot be negative")
                continue

            if flight_ranking_values_obj.equipment_multiplier < 0:
                psg.popup("Equipment score multiplier cannot be negative")
                continue

            if flight_ranking_values_obj.stop_over_score > 0:
                psg.popup("Stop over score cannot be positive")
                continue

            if (
                pnr_ranking_values_obj.loyalties_pplatinum < 0
                or pnr_ranking_values_obj.loyalties_platinum < 0
                or pnr_ranking_values_obj.loyalties_gold < 0
                or pnr_ranking_values_obj.loyalties_silver < 0
                or pnr_ranking_values_obj.ssr_score < 0
                or pnr_ranking_values_obj.pax_cnt_score < 0
                or pnr_ranking_values_obj.first_class_score < 0
                or pnr_ranking_values_obj.business_class_score < 0
                or pnr_ranking_values_obj.eco_class_score < 0
                or pnr_ranking_values_obj.premium_eco_class_score < 0
            ):
                psg.popup("PNR ranking values cannot be negative")
                continue

            window.close()
            break


if __name__ == "__main__":
    initGUI()
