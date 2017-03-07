from flask import Flask
from flask import jsonify
from actions.sendgrid import sendgrid_actions
from auth import requires_auth

# Generate Flask application
app = Flask('looker-data-actions')
app.register_blueprint(sendgrid_actions, url_prefix='/sendgrid')


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
