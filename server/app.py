from flask import Flask
from flask import jsonify
from flask import request
from functools import wraps
from sendgrid_api import send_mail
import os

# Generate Flask application
app = Flask('looker-data-actions')

# Setup Authentication
token = os.getenv('LOOKER_DATA_ACTIONS_TOKEN')


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        r = request.get_json()
        request_token = r.get('data', {}).get('auth')
        if request_token != token:
            return 'Unauthorized Access', 401
        return f(*args, **kwargs)
    return decorated


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=error.description), 404


@app.route("/", methods=['GET'])
@app.route("/ping", methods=['GET'])
def ping():
    return jsonify(app.name)


@app.route("/ping", methods=['POST'])
@requires_auth
def looker_ping():
    response = {
      "looker": {
        "success": True,
        "refresh_query": False
      }
    }
    return jsonify(response)


@app.route("/email/<email>", methods=['POST'])
@requires_auth
def mail(email):
    r = request.get_json()
    subject = r.get('form_params', {}).get('subject')
    body = r.get('form_params', {}).get('body')

    # Send email
    response_code = send_mail(email, subject, body)
    success = response_code == 202

    response = {
      "looker": {
        "success": success,
        "refresh_query": False
      }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
