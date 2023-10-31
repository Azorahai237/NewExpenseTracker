from app import db

class income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    category = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Float, nullable = False)

class expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    category = db.Column(db.String(30), nullable=False)
    amount = db.Column(db.Float, nullable = False)

class goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable = False)
    amount = db.Column(db.Float, nullable = False, unique=True)