import smtplib

def send_mails_bulk(receivers_address, message :str) -> None:
    '''Sends a message as mail to the list of receivers from the sender mail

    :param sender_address: The mail address of the sender
    :param type: str
    :param receivers_address: List of mail addresses of the receivers
    :param type: list[str]
    :param message: The content of the mail
    :param type: str
    :return: none
    
    !!!!ports and host are set for outlook email for testing purposes
    Sender address and mail password are assumed to be same for 
    all mails hence not passed as argument
    '''

    sender_address = '' #sender mail
    sender_mail_pass = '' #sender mail pass
    host = 'smtp-mail.outlook.com'
    port = 587
    subject = "Your Alternate Flight routes"
    bcc_limit = 100
    try:
        for y in range((len(receivers_address)//bcc_limit)+1):
            bcc = ''
            for x in range(bcc_limit):
                if x+y*bcc_limit>=len(receivers_address):
                    break
                    '''
                    this condition is to break the loop when last email of last batch of
                    emails is added to bcc where each batch size is bcc_limit
                    '''
                bcc+=receivers_address[x+y*bcc_limit]+','
            mail = smtplib.SMTP(host , port)
            mail.ehlo()
            mail.starttls()
            mail.login(sender_address, sender_mail_pass)
            header='From:'+sender_address+'\n'+'BCC:'+bcc+'\n'+'subject:'+subject+'\n\n' #!!!!There is no 'to' email address all are bcc
            content=header+message
            mail.sendmail(sender_address, receivers_address, content)
            mail.close()
    except smtplib.SMTPException:
        pass


def send_mail_ind(receivers_address :str, message :str) -> None:
    '''Sends a message as mail to an individual receiver from the sender mail

    :param sender_address: The mail address of the sender
    :param type: str
    :param receivers_address: The mail address of the receiver
    :param type: str
    :param message: The content of the mail
    :param type: str
    :return: none

    !!!!ports and host are set for outlook email for testing purposes
    Sender address and mail password are assumed to be same for 
    all mails hence not passed as argument
    '''
    sender_address = '' #sender mail
    sender_mail_pass = '' #sender mail password
    host = 'smtp-mail.outlook.com'
    port = 587
    subject = "Your Alternate Flight routes"
    try:
        mail = smtplib.SMTP(host , port)
        mail.ehlo()
        mail.starttls()
        mail.login(sender_address, sender_mail_pass)
        header='To:'+receivers_address+'\n'+'From:'+sender_address+'\n'+'subject:'+subject+'\n\n'
        message=header+message
        mail.sendmail(sender_address, receivers_address, message)
        mail.close()
    except smtplib.SMTPException:
        pass
