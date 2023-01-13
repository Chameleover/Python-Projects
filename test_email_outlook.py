import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import creds
import json


def email_new(news_dict):
    message = MIMEMultipart()
    message['Subject'] = "News from today"
    message['From'] = creds.sender
    message['To'] = creds.recipient

    # sendmail() won't accept dict as arg, but accepts a json file
    y = json.dumps(news_dict)
    body = MIMEText(y)
    message.attach(body)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(creds.sender, creds.recipient, message.as_string())