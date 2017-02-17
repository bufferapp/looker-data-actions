from flask import Flask
from flask import jsonify

# Generate Flask application
app = Flask('looker-data-action')


@app.errorhandler(404)
def not_found(error):
    return jsonify(error=error.description), 404


@app.route("/ping/<email>", methods=['GET'])
def ping(email):
    response = {
      "looker": {
        "success": True,
        "refresh_query": True
      }
    }
    app.logger.info(email)
    return jsonify(response)


@app.route('/')
def home():
    return jsonify(status='ok')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
