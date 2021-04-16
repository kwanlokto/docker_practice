import os

from flask import Flask, jsonify
from flask_migrate import MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    DATABASE_URI = (
        "mysql+mysqlconnector://{user}:{password}@{server}/{database}".format(
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            server=os.environ["DB_SERVER"],
            database=os.environ["DB_NAME"],
        )
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

    db.init_app(app)

    manager = Manager(app)
    manager.add_command("db", MigrateCommand)

    with app.app_context():
        from server.routes import account, user  # NOQA: F401

        @app.route("/ping", methods=["GET"])
        def ping():
            return (
                jsonify(
                    isError=False,
                    message="Success",
                    statusCode=200,
                ),
                200,
            )

        return manager
