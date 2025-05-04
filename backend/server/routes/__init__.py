from server.routes.user import *
from server.routes.transaction import *
from server.routes.account import *
from server.routes.server import custom_route
from flask import jsonify

@custom_route("/ping", methods=["GET"])
def ping():
    print("EHLLOO ENTERED!", flush=True)
    return jsonify(
        isError=False,
        message="Success",
        data="status is good",
    )