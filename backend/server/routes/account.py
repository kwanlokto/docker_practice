from flask import jsonify, request

from server.exceptions.db import DBException
from server.models import db
from server.models.account import Account
from server.routes.server import custom_route, require_token


@custom_route("/account", methods=["GET"])
@require_token
def get_account():
    # get all accounts for the user
    accounts = Account.query.filter_by(user_id=request.user.id).all()

    return jsonify(
        isError=False,
        message="Success",
        statusCode=200,
        data=[account.as_dict() for account in accounts],
    )


@custom_route("/account", methods=["POST"])
@require_token
def create_account():
    # add a new account for the user
    name = request.json["name"]

    new_account = Account(name=name, user_id=request.user.id)
    db.session.add(new_account)
    db.session.commit()

    return jsonify(
        isError=False,
        data=new_account.as_dict(),
        message="Added new account to db",
        statusCode=200,
    )


@custom_route("/account/<string:account_id>", methods=["DELETE"])
@require_token
def delete_account(account_id):
    # find the account and ensure it belongs to the current user
    account = Account.query.filter_by(id=account_id, user_id=request.user.id).first()
    if not account:
        raise DBException("Account not found or not authorized")

    db.session.delete(account)
    db.session.commit()

    return jsonify(
        isError=False,
        message="Account deleted successfully",
        statusCode=200,
    )
