import smtplib
import ssl
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from src.classes.output.affected_inventory_sol import AffectedInventorySolution
from src.classes.flight.inventory import Inventory
from src import passenger_dict

from dotenv import load_dotenv

load_dotenv()

email_sender = os.getenv("EMAIL_ID")
email_password = os.getenv("EMAIL_PASSWORD")


def send_mails_bulk(receivers_address: list[str], mail_message: MIMEText) -> None:
    """Sends a message as mail to the list of receivers from the sender mail

    :param receivers_address: List of mail addresses of the receivers
    :param type: list[str]
    :param mail_message: The content of the mail
    :param type: str
    :return: none
    """

    mail_subject = "noreply: Your Alternate Flight Accomodation Routes"
    bcc_limit = 100

    try:
        for batch in range((len(receivers_address) // bcc_limit) + 1):
            em = EmailMessage()
            em.set_content(mail_message)
            em["Subject"] = mail_subject
            em["From"] = email_sender

            context = ssl.create_default_context()

            if (batch + 1) * bcc_limit >= len(receivers_address):
                em["Bcc"] = receivers_address[
                    batch * bcc_limit : len(receivers_address)
                ]
            else:
                em["Bcc"] = receivers_address[
                    batch * bcc_limit : ((batch + 1) * bcc_limit)
                ]

            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(
                    from_addr=email_sender, to_addrs=email_sender, msg=em.as_string()
                )

    except smtplib.SMTPException:
        pass


def create_mime_text_for_default_solution(solution_path: list[Inventory]) -> MIMEText:
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Schedule Update</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        .header {
            background-color: #3498db;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        .content {
            padding: 20px;
        }
        .flight-details {
            margin-top: 20px;
        }
        .path-connecting-flights {
            margin-top: 20px;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Flight Schedule Update</h1>
        </div>
        <div class="content">
            <p>Dear Passenger,</p>
            <p>We hope this message finds you well. We regret to inform you that there have been changes to your upcoming flight schedule due to unforeseen circumstances.</p>
            <div class="path-connecting-flights">
                <p><strong>Updated Flight Path:</strong></p>
                <ol> """

    for index in range(len(solution_path)):
        html = (
            html
            + f"""<li class="flight-details">
            <p><strong>Leg 1:</strong></p>
            <ul>
                <li><strong>Flight Number:</strong>{solution_path[index].flightnumber}</li>
                <li><strong>Departure Airport:</strong>{solution_path[index].departureairport}</li>
                <li><strong>Departure Date and Time:</strong>{solution_path[index].departuredatetime}</li>
                <li><strong>Arrival Airport:</strong>{solution_path[index].arrivalairport}</li>
                <li><strong>Arrival Date and Time:</strong>{solution_path[index].arrivaldatetime}</li>
            </ul>
        </li>"""
        )

    html = (
        html
        + """
                </ol>
            </div>
            <p>Please review the updated flight path and let us know if you have any questions or concerns. We understand that changes to travel plans can be inconvenient, and we appreciate your understanding.</p>
        </div>
        <div class="footer">
            <p>If you have any questions or require further assistance, please contact our customer service team at 
team51763@gmail.com.</p>
            <p>We apologize for any inconvenience caused and appreciate your understanding.</p>
            <p>Safe travels!</p>
            <p>Best regards</p>
        </div>
    </div>
</body>
</html>
"""
    )

    return MIMEText(html, "html")


def create_mime_text_for_other_solutions(
    other_solution_paths: list[list[Inventory]],
) -> MIMEText:
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flight Schedule Update</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        .header {
            background-color: #3498db;
            color: #ffffff;
            text-align: center;
            padding: 20px;
        }
        .content {
            padding: 20px;
        }
        .flight-details {
            margin-top: 20px;
        }
        .path-connecting-flights {
            margin-top: 20px;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
            color: #7f8c8d;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Flight Schedule Update</h1>
        </div>
        <div class="content">
            <p>Dear Passenger,</p>
            <p>We hope this message finds you well. We regret to inform you that flight have been cancelled due to unforeseen circumstances.</p>
            <div class="path-connecting-flights"> """

    for index_1 in range(len(other_solution_paths)):
        html = html + f"""<p><strong>Alternate Flight Path{index_1+1}:</strong></p> """
        for index_2 in range(len(other_solution_paths[index_1])):
            html = (
                html
                + f"""<li class="flight-details">
            <p><strong>Leg {index_2+1}:</strong></p>
            <ul>
                <li><strong>Flight Number:</strong>{other_solution_paths[index_1][index_2].flightnumber}</li>
                <li><strong>Departure Airport:</strong>{other_solution_paths[index_1][index_2].departureairport}</li>
                <li><strong>Departure Date and Time:</strong>{other_solution_paths[index_1][index_2].departuredatetime}</li>
                <li><strong>Arrival Airport:</strong>{other_solution_paths[index_1][index_2].arrivalairport}</li>
                <li><strong>Arrival Date and Time:</strong>{other_solution_paths[index_1][index_2].arrivaldatetime}</li>
            </ul>
        </li>"""
            )
        html = html + "</ol>"

    html = (
        html
        + """
        </div>
        <p>Please review the updated flight path and let us know if you have any questions or concerns. We understand that changes to travel plans can be inconvenient, and we appreciate your understanding.</p>
    </div>
    <div class="footer">
        <p>If you have any questions or require further assistance, please contact our customer service team at team51763@gmail.com.</p>
        <p>We apologize for any inconvenience caused and appreciate your understanding.</p>
        <p>Safe travels!</p>
        <p>Best regards</p>
    </div>
</div>
</body>
</html>
"""
    )

    return MIMEText(html, "html")


def driver_send_mail(final_solutions: list[AffectedInventorySolution]) -> None:
    """Driver function to send mails to the passengers

    :param final_solutions: List of AffectedInventorySolution objects
    :param type: list[AffectedInventorySolution]
    :return: none
    """

    for solution in final_solutions:
        receivers_address_default = []
        for passenger_doc_id in solution.accomodated_passengers:
            receivers_address_default.append(
                passenger_dict[passenger_doc_id].contact_email
            )
        if len(solution.default_solution) != 0:
            mail_message_default = create_mime_text_for_default_solution(
                solution_path=solution.default_solution
            )
        else:
            mail_message_default = MIMEText(
                """Dear Passenger,\nWe regret to inform you that your flight has been cancelled due to unforeseen circumstances.\nNo alternate flight path available
                Sorry for the inconvenience caused.\nBest regards"""
            )
        send_mails_bulk(
            receivers_address=receivers_address_default,
            mail_message=mail_message_default,
        )

        receivers_address_other = []
        for passenger_doc_id in solution.unaccomodated_passengers:
            receivers_address_other.append(
                passenger_dict[passenger_doc_id].contact_email
            )
        if(len(solution.other_solutions) != 0):
            mail_message_other = create_mime_text_for_other_solutions(
                other_solution_paths=solution.other_solutions
            )
        else:
            mail_message_other = MIMEText(
                """Dear Passenger,\nWe regret to inform you that your flight has been cancelled due to unforeseen circumstances.\nNo alternate flight path available
                Sorry for the inconvenience caused.\nBest regards"""
            )
        send_mails_bulk(
            receivers_address=receivers_address_other, mail_message=mail_message_other
        )
