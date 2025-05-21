from functools import wraps

from definitions import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB, JWT_SECRET
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
DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

webserver.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

# Initialize extensions
db.init_app(webserver)
Migrate(webserver, db)

webserver.config["JWT_SECRET_KEY"] = JWT_SECRET  # Change this to a more secure key
webserver.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Set expiration time for access token

jwt = JWTManager(webserver)

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'message': 'Token has expired',
        'statusCode': 401,
        'isError': True
    }), 401

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
                resp_body = jsonify(message=str(err))
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
