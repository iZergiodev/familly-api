from flask import Flask, request, jsonify
from models import Todo
from extension import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo_list.db"

db.init_app(app)

with app.app_context():
    db.create_all()

#Crear rutas

@app.route('/todos', methods = ['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify({'todos': [todo.serialize() for todo in todos]})

@app.route('/todos', methods = ['POST'])
def create_todo():
    data = request.get_json()
    todo = Todo(done = data['done'], label = data['label'])
    db.session.add(todo)
    db.session.commit()

    return jsonify({'message':'Todo creado con éxito', 'todo': todo.serialize()}), 201

@app.route('/todos/<int:id>', methods = ['GET'])
def get_todo(id):
    todo = Todo.query.get(id)
    if not todo:
        return jsonify({'message':'Todo no encontrado'}), 404
    return jsonify(todo.serialize())

