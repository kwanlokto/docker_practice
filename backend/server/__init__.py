import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask.cli import with_appcontext
import click
from server.routes import register_routes
from flask_jwt_extended import JWTManager
from server.models import db
from datetime import timedelta

# Initialize database

def create_app():
    app = Flask(__name__)
    CORS(app, resources=r"/*")

    # Configure Database URI
    DATABASE_URI = (
        "mysql+mysqlconnector://{user}:{password}@{server}/{database}".format(
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASS"],
            server=os.environ["DB_SERVER"],
            database=os.environ["DB_NAME"],
        )
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)

    app.config["JWT_SECRET_KEY"] = "your_secret_key"  # Change this to a more secure key
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Set expiration time for access token

    JWTManager(app)

    # Register CLI commands
    @app.cli.command("db_create")
    @with_appcontext
    def db_create():
        """Create the database tables."""
        db.create_all()
        click.echo("Database tables created.")

    @app.cli.command("db_drop")
    @with_appcontext
    def db_drop():
        """Drop all database tables."""
        db.drop_all()
        click.echo("Database tables dropped.")

    # Example of an additional command for running migrations (optional)
    @app.cli.command("db_migrate")
    @with_appcontext
    def db_migrate():
        """Run database migrations."""
        from flask_migrate import upgrade
        upgrade()
        click.echo("Migrations applied.")

    # Routes and error handling
    with app.app_context():
        register_routes(app)

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

        @app.errorhandler(500)
        def server_error(e):
            logging.exception("An error occurred during a request. %s", e)
            return "An internal error occurred", 500

    return app
