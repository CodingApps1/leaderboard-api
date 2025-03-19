from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, default=0)
    address = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
