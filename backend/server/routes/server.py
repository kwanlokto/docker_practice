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
DATABASE_URI = "mysql+mysqlconnector://{user}:{password}@{server}/{database}".format(
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    server=os.environ["DB_SERVER"],
    database=os.environ["DB_NAME"],
)
webserver.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

# Initialize extensions
db.init_app(webserver)
Migrate(webserver, db)

webserver.config["JWT_SECRET_KEY"] = "your_secret_key"  # Change this to a more secure key
webserver.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Set expiration time for access token

JWTManager(webserver)

# def validate_security_token(function_reference):
#     """
#     Used to handle route security
#     """
#     token = None
#     if "ss_auth" in request.headers:
#         token = request.headers["ss-auth"]

#     if not token:
#         token_issue(function_reference, "Security token missing", request.remote_addr)

#     try:
#         decode(token, JWT_SECRET, algorithms=[JWT_ALG])

#         # This data should be available but it is currently not used
#         # machine_id = data['machine_id']
#     except Exception as err:
#         error_message = f"Token is invalid. {str(err)}"
#         token_issue(function_reference, error_message, request.remote_addr)


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
                # log_message(
                #     f"Time: {datetime.now().strftime('%H:%M:%S')}\n"
                #     f"Function: {str(function_reference.__name__)}\n"
                #     f"{type(err).__name__}: {str(err)}\n"
                #     f"Message: {traceback.format_exc()}\n"
                # )

            return (resp_body, status_code)

        return wrapper

    return decorator


# def token_issue(function_reference, issue_type, request_ip):
#     """
#     Helper used to standardize logging and responses to token issues. This will log a message and
#     return a response.

#     Parameters:
#         issue_type (string): Type of issue with request security token. This will be used for the
#         logs and response.
#         request_ip (stirng): The address of the client sending the request.

#     Returns:
#         (Tuple) Response body and status code for a flask response.

#     """

#     log_message(
#         f"Time: {datetime.now().strftime('%H:%M:%S')}\n"
#         f"Function: {str(function_reference.__name__)}\n"
#         f"Type: {issue_type}\n"
#         f"IP: {request_ip}\n"
#     )

#     raise SecurityException(issue_type)
