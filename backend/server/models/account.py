from server.models import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    balance = db.Column(db.Numeric, default=0)

    def __repr__(self):
        return f"<Account {self.username}>"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
