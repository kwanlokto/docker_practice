from flask import current_app as app
from flask import jsonify, request
from server import db
from server.models.user import User


@app.route("/user/signup", methods=["POST"])
def userSignup():
    """
    Create a new user
    """
    try:
        request_data = request.get_json()
        first_name = request_data["first_name"]
        last_name = request_data["last_name"]
        email = request_data["email"]

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

    new_user = User(first_name=first_name, last_name=last_name, email=email)
    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            isError=False,
            message="Added new user to db",
            statusCode=200,
        ),
        200,
    )


@app.route("/user/login", methods=["POST"])
def userLogin():
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
    except Exception as e:
        return (
            jsonify(
                isError=True,
                message=f"Missing User from DB. {e}",
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
