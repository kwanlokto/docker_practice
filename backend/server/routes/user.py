from flask import jsonify, request
from server.models import db
from server.exceptions.db import DBException
from server.models.user import User
from server.routes.server import custom_route
from flask_jwt_extended import create_access_token


@custom_route("/user/signup", methods=["POST"])
def user_signup():
    """
    Create a new user
    """
    try:
        request_data = request.get_json()
        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        email = request_data["email"]
        password = request_data["password"]

        new_user = User(first_name=first_name, last_name=last_name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
    except KeyError as err:
        msg = f"Missing required field: {err}"
        raise Exception(msg)
    except Exception as err:
        raise DBException(err)

    return jsonify(
        isError=False,
        message="Added new user to db",
        statusCode=200,
    )


@custom_route("/user/login", methods=["POST"])
def user_login():
    try:
        request_data = request.get_json()
        email = request_data["email"]
        password = request_data["password"]
        user = User.query.filter_by(email=email).one()
        if not user.check_password(password):
            raise Exception("Incorrect password")

        # Create session using ORM
        token = create_access_token(identity=user.id)
        user.access_token = (
            token  # Store token in DB if needed for revocation/validation
        )
        db.session.commit()
    except KeyError as err:
        msg = f"Missing required field: {err}"
        raise Exception(msg)
    except Exception as err:
        raise DBException(err)

    return jsonify(
        isError=False,
        message="Login successful",
        statusCode=200,
        data={"user": user.as_dict(), "token": token},
    )
