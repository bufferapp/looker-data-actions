import sendgrid
import os

from sendgrid.helpers.mail import Email, Content, Mail

# Grab environmental variables
api_key = os.environ.get('SENDGRID_API_KEY')
from_email = os.environ.get('SENDGRID_ACCOUNT_EMAIL')

# Instanciate API client
sg = sendgrid.SendGridAPIClient(apikey=api_key)


def send_mail(to, subject, body):
    to_email = Email(to)
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
