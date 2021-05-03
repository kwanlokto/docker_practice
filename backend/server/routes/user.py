from flask import current_app as app
from flask import jsonify, request

from server import db
from server.models.user import User


@app.route("/user", methods=["POST"])
def user():
    """
    Create a new user
    """
    try:
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")

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
