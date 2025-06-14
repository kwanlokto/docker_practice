from flask import jsonify

from server.routes.account import *
from server.routes.server import custom_route
from server.routes.transaction import *
from server.routes.user import *


@custom_route("/ping", methods=["GET"])
def ping():
    return jsonify(
        isError=False,
        message="Success",
        data="status is good",
    )
