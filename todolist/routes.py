from flask import flash, redirect, render_template, request, url_for
from todolist import db
from todolist.forms import ToDoList
from todolist.models import ToDo
from flask import current_app as app
#from models import ToDo

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
        flash(f'To Do created successfully')
        return redirect(url_for('home'))
    return render_template('createtodolist.html', title='Create To Do', form=form)


@app.route('/viewtodo')
def view_todolist():
    all_todo = ToDo.query.all()

    return render_template('viewtodo.html', title='View To Do', data=all_todo)