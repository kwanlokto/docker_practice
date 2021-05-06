import random
import string

from flask import current_app as app
from flask import jsonify, request
from server import db
from server.models.account import Account
from server.models.user import User


@app.route("/user/<string:user_id>/account", methods=["GET", "POST"])
def account(user_id):
    if request.method == "GET":
        # get all accounts for the user
        accounts = Account.query.join(User).filter_by(id=user_id).all()
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


@app.route("/user/<string:user_id>/account/token", methods=["GET", "PUT"])
def accountToken(user_id):
    if request.method == "GET":
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
        # get all accounts for the user
        account = (
            Account.query.filter_by(username=username)
            .join(User)
            .filter_by(id=user_id)
            .one()
        )
        if account.check_password(password):
            return (
                jsonify(
                    isError=False,
                    message="Success",
                    statusCode=200,
                    data=account.access_token,
                ),
                200,
            )
        return (
            jsonify(
                isError=True,
                message="Incorrect Username or Password",
                statusCode=401,
            ),
            400,
        )
    elif request.method == "PUT":
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

        account = (
            Account.query.filter_by(username=username)
            .join(User)
            .filter_by(id=user_id)
            .one()
        )

        if account.check_password(password):
            letters = string.ascii_letters  # new access token
            access_token = "".join(random.choice(letters) for i in range(10))
            account.access_token = access_token
            db.session.commit()
            return (
                jsonify(
                    isError=False,
                    message="Success",
                    statusCode=200,
                    data=access_token,
                ),
                200,
            )
        return (
            jsonify(
                isError=True,
                message="Incorrect Username or Password",
                statusCode=401,
            ),
            400,
        )
