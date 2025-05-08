import os
import traceback
from datetime import datetime
from functools import wraps

from definitions import JWT_ALG, JWT_SECRET
from flask import Flask, jsonify, request
from flask_cors import CORS
from jwt import decode
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.models import db
from datetime import timedelta

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
                resp_body = jsonify(message=err.message, title=err.title)
                status_code = err.status_code
            except Exception as err:
                resp_body = jsonify(message="[Cloud API] Internal server error.")
                status_code = 500

            return (resp_body, status_code)

        return wrapper

    return decorator
