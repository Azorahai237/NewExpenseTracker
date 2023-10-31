from app import db, models

entry = db.session.query(models.goal).first()


print(entry.amount)