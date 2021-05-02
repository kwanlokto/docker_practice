import json

from flask import current_app as app
from flask import jsonify, request

from server import db
from server.models.account import Account
from server.models.user import User


@app.route("/user/<string:user_id>/account", methods=["GET", "POST"])
def account(user_id):
    if request.method == "GET":
        # get all accounts for the user
        accounts = User.query.filter_by(id=user_id).join(Account).all()
        return (
            jsonify(
                isError=False,
                message="Success",
                statusCode=200,
                data=[account.as_dict() for account in accounts],
            ),
            200,
        )

    elif request.method == "POST":
        # add a new account for the user
        try:
            username = request.form["username"]
            password = request.form["password"]

        except KeyError:
            return (
                jsonify(
                    isError=True,
                    message="Missing username or password",
                    statusCode=400,
                ),
                400,
            )
        new_account = Account(username=username, user_id=user_id)
        new_account.set_password(password)
        db.session.add(new_account)
        db.session.commit()

        return (
            jsonify(
                isError=False,
                message="Added new account to db",
                statusCode=200,
            ),
            200,
        )
