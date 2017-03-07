from functools import wraps
from flask import request
import os

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
