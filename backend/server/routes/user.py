from flask import jsonify, request, Blueprint
from server.models import db
from server.models.user import User
user_bp = Blueprint('user', __name__)


@user_bp.route("/user/signup", methods=["POST"])
def user_signup():
    """
    Create a new user
    """
    try:
        request_data = request.get_json()
        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        email = request_data["email"]

        new_user = User(first_name=first_name, last_name=last_name, email=email)
        db.session.add(new_user)
        db.session.commit()
    except KeyError as err:
        msg = f"Failed to create user. ${err}"
        return (
            jsonify(
                isError=True,
                message=msg,
                statusCode=400,
            ),
            400,
        )
    except Exception as err:
        return (
            jsonify(
                isError=True,
                message=str(err),
                statusCode=409,
            ),
            409,
        )

    return (
        jsonify(
            isError=False,
            message="Added new user to db",
            statusCode=200,
        ),
        200,
    )


@user_bp.route("/user/login", methods=["POST"])
def user_login():
    try:
        request_data = request.get_json()
        email = request_data["email"]
        user = User.query.filter_by(email=email).one()

    except KeyError as err:
        msg = f"Failed to get user. ${err}"
        return (
            jsonify(
                isError=True,
                message=msg,
                statusCode=400,
            ),
            400,
        )
    except Exception as err:
        return (
            jsonify(
                isError=True,
                message=f"Missing User from DB. {err}",
                statusCode=401,
            ),
            401,
        )
    return (
        jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data=user.as_dict(),
        ),
        200,
    )
