from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.Text(2000000), nullable=False)