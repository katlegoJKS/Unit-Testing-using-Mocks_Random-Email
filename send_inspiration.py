import os
import smtplib

SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = os.environ.get('SMTP_PORT')
EMAIL_LOGIN = os.environ.get('EMAIL_LOGIN')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_TO = os.environ.get('EMAIL_TO')

def send_email():
    try:
        inspirational_quote = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        inspirational_quote.ehlo()
        inspirational_quote.starttls()
        inspirational_quote.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        inspirational_quote.sendmail(EMAIL_LOGIN, EMAIL_TO, 'Subject: So long.\n"The only true measure of success if the number of people you have helped" Ray Dalio')
        inspirational_quote.quit()
        return "Message successfully sent"
    else:
        return "Sending message was unsuccessful"

send_email()