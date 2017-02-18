from flask import Flask
from flask import jsonify
from flask import request
import os
from flask_httpauth import HTTPTokenAuth


# Generate Flask application
app = Flask('looker-data-action')

# Setup Authentication
auth = HTTPTokenAuth(scheme='Bearer')
token = os.getenv('TOKEN')


@auth.verify_token
def verify_token(t):
    if t == token:
        return True
    return False


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=error.description), 404


@app.route("/ping/<email>", methods=['POST'])
@auth.login_required
def ping(email):
    app.logger.info(request.get_json())
    app.logger.info(email)
    response = {
      "looker": {
        "success": True,
        "refresh_query": True
      }
    }
    return jsonify(response)


@app.route('/')
@auth.login_required
def home():
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
