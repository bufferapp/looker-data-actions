import sendgrid
import os

from sendgrid.helpers.mail import Email, Content, Mail

api_key = os.environ.get('SENDGRID_API_KEY')
sg = sendgrid.SendGridAPIClient(apikey=api_key)
from_email = Email('davidgasquez@gmail.com')


def send_mail(to, subject, body):
    to_email = Email('davidgasquez@gmail.com')
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code
