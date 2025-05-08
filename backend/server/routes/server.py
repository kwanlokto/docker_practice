import os
import traceback
from datetime import datetime
from functools import wraps

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
from server.models.user import User
from server.models import db
from datetime import timedelta
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

# Flask web server definition
webserver = Flask(__name__)
CORS(webserver)
# Configure Database URI
DATABASE_URI = "postgresql+psycopg2://{user}:{password}@{server}/{database}".format(
    user=os.environ["POSTGRES_USER"],
    password=os.environ["POSTGRES_PASSWORD"],
    server=os.environ["POSTGRES_SERVER"],
    database=os.environ["POSTGRES_DB"],
)

webserver.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

# Initialize extensions
db.init_app(webserver)
Migrate(webserver, db)

webserver.config["JWT_SECRET_KEY"] = "your_secret_key"  # Change this to a more secure key
webserver.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Set expiration time for access token

JWTManager(webserver)


def custom_route(rule, **options):
    """
    Custom Route decorator to handle different exceptions being raised
    """

    def decorator(function_reference):
        @webserver.route(f"{rule}", **options)
        @wraps(function_reference)
        def wrapper(*args, **kwargs):
            try:
                resp_body = function_reference(*args, **kwargs)
                status_code = 200
            except Exception as err:
                resp_body = jsonify(message=err.message)
                status_code = 500

            return (resp_body, status_code)

        return wrapper

    return decorator

def require_token(f):
    @jwt_required()
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.filter_by(id=user_id).one_or_none()
        if not user:
            raise Exception(f"Failed to find {user_id} in the system")

        incoming_token = request.headers.get("Authorization", "").replace("Bearer ", "")
        if user.access_token != incoming_token:
            raise Exception("Token mismatch")

        request.user = user  # attach user info to the request for downstream use
        return f(*args, **kwargs)
    return decorated_function
