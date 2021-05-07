from flask import current_app as app
from flask import jsonify, request
from server import db
from server.models.account import Account
from server.models.transaction import Transaction
from server.models.user import User


@app.route(
    "/user/<string:user_id>/account/<string:account_id>/transaction",
    methods=["GET", "POST"],
)
def transaction(user_id, account_id):
    if request.method == "GET":
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

    elif request.method == "POST":
        # add a new transaction for the account
        try:
            request_data = request.get_json()
            operation = request_data["operation"]
            value = request_data["value"]

        except KeyError:
            return (
                jsonify(
                    isError=True,
                    message="Missing value or operation type",
                    statusCode=400,
                ),
                400,
            )
        new_transaction = Transaction(
            account_id=account_id, operation=operation, value=value
        )
        db.session.add(new_transaction)
        db.session.commit()

        return (
            jsonify(
                isError=False,
                message="Added new transaction to db",
                statusCode=200,
            ),
            200,
        )
