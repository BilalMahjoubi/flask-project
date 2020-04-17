from flask import Flask,request, render_template, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid


app=Flask(__name__)


app.config['SECRET_KEY']="secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost/todo'
db=SQLAlchemy(app)
class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    texte= db.Column(db.String(50))
    complete =db.Column(db.Boolean)


@app.route('/todo', methods=['GET'])
def get_all_todo():
    todos = Todo.query.all()
    output= []
    for todo in todos :
        todo_data = {}
        todo_data['id']=todo.id
        todo_data['texte']=todo.texte
        todo_data['complete']=todo.complete
        output.append(todo_data)
    return jsonify({'todos' : output})

@app.route('/todo/<id>', methods=['GET'])
def getTodo(id):
    todo = Todo.query.filter_by(id=id).first()

    if not todo:
        return jsonify({'message': 'No Todo found'})
    
    todo_data = {}
    todo_data['id']=todo.id
    todo_data['texte']=todo.texte
    todo_data['complete']=todo.complete
    return jsonify(todo_data)

@app.route('/todo', methods=['POST'])
def createTodo():
    data=request.get_json()
    new_todo=Todo(texte=data['texte'],complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'message': "Todo create"})

@app.route('/todo/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if not todo:
        return jsonify({'message' : 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message' : 'Tâche terminée!'})


@app.route('/todo/<id>', methods=['PUT'])
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first()
    if not todo:
        return jsonify({'message': 'No Todo found'})
    todo.complete=True
    db.session.commit()
    return jsonify({'message': 'tâche terminée !'})



    
    
if __name__ == "__main__":
        app.run(debug=True)

