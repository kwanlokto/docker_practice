from server.routes.user import user_bp
from server.routes.transaction import transaction_bp
from server.routes.account import account_bp


def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(transaction_bp, url_prefix='/api')
    app.register_blueprint(account_bp, url_prefix='/api')