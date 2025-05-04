import random
import string

from flask import jsonify, request, Blueprint
from server.models import db
from server.models.account import Account
from server.models.user import User
from server.routes.server import custom_route



@custom_route("/user/<string:user_id>/account", methods=["GET"])
def account(user_id):
    # get all accounts for the user
    accounts = Account.query.join(User).filter_by(id=user_id).all()
    return jsonify(
        isError=False,
        message="Success",
        statusCode=200,
        data=[account.as_dict() for account in accounts],
    )
    

@custom_route("/user/<string:user_id>/account", methods=["POST"])
def create_account():
    # add a new account for the user
    try:
        request_data = request.get_json()
        username = request_data["username"]
        password = request_data["password"]

        new_account = Account(username=username)
        new_account.set_password(password)
        db.session.add(new_account)
        db.session.commit()
    except KeyError:
        return jsonify(
            isError=True,
            message="Missing username or password",
            statusCode=400,
        )
    except Exception as err:
        raise err

    return jsonify(
        isError=False,
        message="Added new account to db",
        statusCode=200,
    )


@custom_route("/user/<string:user_id>/account/token", methods=["GET"])
def get_account_token(user_id):
    request_data = request.get_json()
    try:
        username = request_data["username"]
        password = request_data["password"]
        # get all accounts for the user
        account = (
            Account.query.filter_by(username=username)
            .join(User)
            .filter_by(id=user_id)
            .one()
        )
    except KeyError:
        return jsonify(
            isError=True,
            message="Missing username or password",
            statusCode=400,
        )
    except Exception as err:
       raise Exception
    if account.check_password(password):
        return jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data=account.access_token,
        )
    return jsonify(
        isError=True,
        message="Incorrect Username or Password",
        statusCode=401,
    )

@custom_route("/user/<string:user_id>/account/token", methods=[ "PUT"])
def update_account_token(user_id):
    request_data = request.get_json()

    try:
        username = request_data["username"]
        password = request_data["password"]
        account = (
            Account.query.filter_by(username=username)
            .join(User)
            .filter_by(id=user_id)
            .one()
        )
    except KeyError:
        return jsonify(
            isError=True,
            message="Missing username or password",
            statusCode=400,
        )
    except Exception as err:
        return jsonify(
            isError=True,
            message=f"Missing Account from DB. {err}",
            statusCode=401,
        )

    if account.check_password(password):
        letters = string.ascii_letters  # new access token
        access_token = "".join(random.choice(letters) for i in range(10))
        account.access_token = access_token
        db.session.commit()
        return jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data=access_token,
        )
    return jsonify(
        isError=True,
        message="Incorrect Username or Password",
        statusCode=401,
    )
