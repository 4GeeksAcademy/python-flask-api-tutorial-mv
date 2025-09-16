from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route('/todos', methods=['GET'])
def handle_todos():
    """GET /todos - Return the list of all todos"""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    """POST /todos - Add a new todo and return updated list"""
    request_body = request.get_json()
    
    # Add the new todo to the list
    todos.append(request_body)
    
    # Return the updated list of todos
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """DELETE /todos/<int:position> - Remove todo by position and return updated list"""
    
    # Remove the todo at the specified position
    todos.pop(position)
    
    # Return the updated list of todos
    return jsonify(todos)

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)