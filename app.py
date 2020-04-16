from flask import Flask,request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/bilal/Desktop/flask-project/todo.db'
db=SQLAlchemy(app)
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    texte= db.Column(db.String(50))
    compplete =db.Column(db.Boolean)

@app.route('/')
def index():
    complet=Todo.query.filter_by(compplete=False).all()
    incomplet=Todo.query.filter_by(compplete=True).all()


    return render_template('index.html', complet=complet, incomplet=incomplet)
@app.route('/add', methods=['POST'])
def add():
    todo= Todo(texte=request.form['todoitem'], compplete=False)
    db.session.add(todo)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/update/<id>')
def update(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.compplete=True
    db.session.commit()    
    return redirect(url_for('index'))



if __name__ == "__name__":
    app.run(debug=True)

