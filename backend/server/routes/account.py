import random
import string

from flask import jsonify, request, Blueprint
from server.models import db
from server.models.account import Account
from server.models.user import User
from server.routes.server import custom_route


@custom_route("/user/<string:user_id>/account", methods=["GET"])
def get_account(user_id):
    # get all accounts for the user
    accounts = Account.query.filter_by(user_id=user_id).all()

    return jsonify(
        isError=False,
        message="Success",
        statusCode=200,
        data=[account.as_dict() for account in accounts],
    )


@custom_route("/user/<string:user_id>/account", methods=["POST"])
def create_account():
    # add a new account for the user
    name = request.json["name"]

    new_account = Account(name=name)
    db.session.add(new_account)
    db.session.commit()

    return jsonify(
        isError=False,
        message="Added new account to db",
        statusCode=200,
    )
