import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import creds


def email_new(df):

    # instantiate MIMEText object
    message = MIMEMultipart("Alternative")
    message['Subject'] = "News from today"
    message['From'] = creds.sender
    message['To'] = creds.recipient
    body = MIMEText(df, "html")

    message.attach(body)

    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(creds.sender, creds.recipient, message.as_string())
        print("email send successfully")
