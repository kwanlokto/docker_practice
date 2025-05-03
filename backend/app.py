from flask import Flask
from routes import register_blueprints
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)