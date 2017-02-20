import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Mail
from flask import Blueprint

sendgrid_api = Blueprint('sendgrid_api', __name__)


@sendgrid_api.route("/sendgrid")
def accountList():
    return "list of accounts"
