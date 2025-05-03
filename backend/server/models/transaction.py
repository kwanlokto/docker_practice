from server.models import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    operation = db.Column(db.String(20), nullable=False)
    value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Transaction {self.operation} >"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
