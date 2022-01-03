import os
from flask import Flask, flash, redirect, render_template, request, url_for
from forms import ToDoList
from flask_sqlalchemy import SQLAlchemy
#from models import ToDo

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '45145gfr4tg'
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}/todo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.Text(2000000), nullable=False)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")


@app.route('/createtodo', methods=["GET", "POST"])
def create_todolist():
    form = ToDoList()
    if request.method == "POST":
        if form.validate_on_submit():
            to_do = ToDo(to_do=form.todo.data)
        db.session.add(to_do)
        db.session.commit()
        flash(
            f'To Do created successfully')
        return redirect(url_for('home'))

    return render_template('createtodolist.html', title='Create To Do', form=form)


@app.route('/viewtodo')
def view_todolist():
    all_todo = ToDo.query.all()

    return render_template('viewtodo.html', title='View To Do', data=all_todo)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
