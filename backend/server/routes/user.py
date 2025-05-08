from flask import jsonify, request
from server.models import db
from server.models.user import User
from server.routes.server import custom_route


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
        msg = f"Failed to create user. ${err}"
        return jsonify(
            isError=True,
            message=msg,
            statusCode=400,
        )
    except Exception as err:
        return jsonify(
            isError=True,
            message=str(err),
            statusCode=409,
        )

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

    except KeyError as err:
        msg = f"Failed to get user. ${err}"
        return jsonify(
            isError=True,
            message=msg,
            statusCode=400,
        )
    except Exception as err:
        return jsonify(
            isError=True,
            message=f"Missing User from DB. {err}",
            statusCode=401,
        )
    return jsonify(
        isError=False,
        message="Success",
        statusCode=200,
        data=user.as_dict(),
    )
