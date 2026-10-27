
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
todo_id_counter = 1


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    global todo_id_counter

    data = request.get_json()

    todo_item = {
        "id": todo_id_counter,
        "task": data.get('task'),
        "done": False
    }

    todos.append(todo_item)
    todo_id_counter += 1

    return jsonify(todo_item), 201


@app.route('/todos/<int:todo_id>/done', methods=['PUT'])
def mark_done(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = True
            return jsonify(todo)

    return jsonify({"error": "Item not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)