from pymysql import Date
from app import db
from datetime import datetime

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.Text(2000000), nullable=False)
    date_created = db.Column(db.Date(120), default=datetime.utcnow)