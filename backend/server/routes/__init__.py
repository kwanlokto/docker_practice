from server.routes.user import *
from server.routes.transaction import *
from server.routes.account import *
from server.routes.server import custom_server
from flask import jsonify

@custom_route("/ping", methods=["GET"])
def ping():
    return (
        jsonify(
            isError=False,
            message="Success",
            statusCode=200,
        ),
        200,
    )