import sendgrid
import os
from auth import requires_auth
from flask import Blueprint
from flask import jsonify
from flask import request
from sendgrid.helpers.mail import Email, Content, Mail

# Create Blueprint
sendgrid_actions = Blueprint('sendgrid_actions', 'sendgrid_actions')

# Grab environmental variables
api_key = os.environ.get('SENDGRID_API_KEY')
from_email = Email(os.environ.get('SENDGRID_ACCOUNT_EMAIL'))

# Instanciate API client
sg = sendgrid.SendGridAPIClient(apikey=api_key)


@sendgrid_actions.route("/email/<email>", methods=['POST'])
@requires_auth
def send_mail(email):
    r = request.get_json()
    subject = r.get('form_params', {}).get('subject')
    body = r.get('form_params', {}).get('body')

    # Send email
    to_email = Email(email)
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    success = response.status_code == 202

    response = {
      "looker": {
        "success": success,
        "refresh_query": False
      }
    }
    return jsonify(response)
