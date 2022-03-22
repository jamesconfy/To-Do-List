from todolist import db
from datetime import datetime


class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.Text(2000000), nullable=False)
    date_created = db.Column(db.Date, default=datetime.utcnow)