import smtplib

def send_mails_bulk(receivers_address :list[str], mail_message :str) -> None:
    '''Sends a message as mail to the list of receivers from the sender mail

    :param receivers_address: List of mail addresses of the receivers
    :param type: list[str]
    :param mail_message: The content of the mail
    :param type: str
    :return: none
    
    !!!!ports and host are set for outlook email currently
    Sender address and mail password are assumed to be same for 
    all mails hence not passed as argument
    '''

    sender_mail_address = '' #sender mail
    sender_mail_pass = '' #sender mail pass
    host = 'smtp-mail.outlook.com'
    port = 587
    mail_subject = "Your Alternate Flight routes"
    bcc_limit = 100
    try:
        for batch in range((len(receivers_address)//bcc_limit)+1):
            mail = smtplib.SMTP(host , port)
            mail.ehlo()
            mail.starttls()
            mail.login(sender_mail_address, sender_mail_pass)
            mail_header='From:'+sender_mail_address+'\n'+'subject:'+mail_subject+'\n\n' #!!!!There is no 'to' email address all are bcc
            content=mail_header+mail_message
            
            if (batch+1)*bcc_limit >= len(receivers_address):
                mail.sendmail(sender_mail_address, receivers_address[batch*bcc_limit:len(receivers_address)], content)
            else :
                mail.sendmail(sender_mail_address, receivers_address[batch*bcc_limit:((batch+1)*bcc_limit)], content)
            
        mail.close()
    except smtplib.SMTPException:
        pass


def send_mail_individual(receivers_address :str, mail_message :str) -> None:
    '''Sends a message as mail to an individual receiver from the sender mail

    :param receivers_address: The mail address of the receiver
    :param type: str
    :param mail_message: The content of the mail
    :param type: str
    :return: none

    !!!!ports and host are set for outlook email currently
    Sender address and mail password are assumed to be same for 
    all mails hence not passed as argument
    '''
    sender_mail_address = '' #sender mail
    sender_mail_pass = '' #sender mail password
    host = 'smtp-mail.outlook.com'
    port = 587
    mail_subject = "Your Alternate Flight routes"
    try:
        mail = smtplib.SMTP(host , port)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_mail_address, sender_mail_pass)
        mail_header='To:'+receivers_address+'\n'+'From:'+sender_mail_address+'\n'+'subject:'+mail_subject+'\n\n'
        mail_message=mail_header+mail_message
        mail.sendmail(sender_mail_address, receivers_address, mail_message)
        mail.close()
    except smtplib.SMTPException:
        pass
