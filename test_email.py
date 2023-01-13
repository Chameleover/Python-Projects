
import creds
from email.message import EmailMessage
import smtplib


def send_email(news_dict):
    message = EmailMessage()
    message['Subject'] = "New Data from Today test_email.py"
    message['From'] = creds.sender
    message['To'] = creds.recipient
    body = '''
    email body //yeah
    '''

    message.set_content(body)
    # Add security
    #context = ssl.create_default_context()

    with smtplib.SMTP("smtp.office365.com", 465) as smtp:
        smtp.login(creds.sender, creds.password)
        smtp.sendmail(creds.sender, creds.recipient, body)





