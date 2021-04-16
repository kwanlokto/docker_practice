from server import db
from werkzeug.security import check_password_hash, generate_password_hash


class Account(db.Model):
    username = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Account %r>" % self.username
