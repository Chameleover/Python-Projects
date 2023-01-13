# DONT TOUCH THIS CODE, it actually sends an email :D


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import creds
import pandas as pd




def email_new():

    # read news file



    ## WORKING, but does not include hyperlinks:
    df = pd.read_excel("news.xlsx", header=None)
    html_body = f"""<h1> News report </h1> {df.to_html(render_links=True)}"""

    # instantiate MIMEText object
    message = MIMEText(html_body, 'html', 'utf-8')
    message['Subject'] = "News from today"
    message['From'] = creds.sender
    message['To'] = creds.recipient



    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()
        server.login(creds.sender, creds.password)
        server.sendmail(creds.sender, creds.recipient, message.as_string())


email_new()