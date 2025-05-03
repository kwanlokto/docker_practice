from flask import jsonify, request, Blueprint
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import NoResultFound
import time
import random

from server.models import db
from server.models.account import Account
from server.models.transaction import Transaction
from server.models.user import User

transaction_bp = Blueprint('products', __name__)

MAX_RETRIES = 3
RETRY_DELAY_RANGE = (0.1, 0.5)  # seconds

@transaction_bp.route(
    "/user/<string:user_id>/account/<string:account_id>/transaction",
    methods=["GET"],
)
def get_transaction(user_id, account_id):
    # get all transactions for the selected account
    transactions = (
        Transaction.query.join(Account)
        .filter_by(id=account_id)
        .join(User)
        .filter_by(id=user_id)
        .all()
    )
    return (
        jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data=[transaction.as_dict() for transaction in transactions],
        ),
        200,
    )

@transaction_bp.route(
    "/user/<string:user_id>/account/<string:account_id>/transaction",
    methods=["POST"],
)
def create_transaction(user_id, account_id):
    try:
        request_data = request.get_json()
        operation = request_data["operation"]
        value = request_data["value"]

        for attempt in range(MAX_RETRIES):
            try:
                with db.session.begin_nested():  # Use SAVEPOINT for retries
                    # Lock the account row
                    db.session.query(Account).filter_by(id=account_id).with_for_update()

                    new_transaction = Transaction(
                        account_id=account_id,
                        operation=operation,
                        value=value,
                    )
                    db.session.add(new_transaction)

                db.session.commit()
                return jsonify({
                    "isError": False,
                    "message": "Transaction completed",
                    "statusCode": 200,
                }), 200

            except OperationalError as e:
                if "deadlock detected" in str(e).lower() and attempt < MAX_RETRIES - 1:
                    db.session.rollback()
                    delay = random.uniform(*RETRY_DELAY_RANGE)
                    time.sleep(delay)
                    continue  # retry
                else:
                    raise

    except KeyError:
        return jsonify({
            "isError": True,
            "message": "Missing required field",
            "statusCode": 400,
        }), 400

    except NoResultFound:
        return jsonify({
            "isError": True,
            "message": "Account not found",
            "statusCode": 404,
        }), 404

    except Exception as err:
        db.session.rollback()
        return jsonify({
            "isError": True,
            "message": f"Transaction failed: {str(err)}",
            "statusCode": 500,
        }), 500

