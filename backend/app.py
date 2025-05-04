from server.routes.server import webserver
from definitions import APP_ENV


if __name__ == "__main__":
    webserver.run(
        host="0.0.0.0",
        port=5000,
        debug=APP_ENV == "development",
    )
