from flask import Flask, request, jsonify
from models.task import Task
import uuid

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(id=str(uuid.uuid4()),title=data['title'], description=data.get('description', ''))
    tasks.append(new_task)
    return jsonify({
        "message": 'Task successfully created!'
    })

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    return jsonify({
        "tasks": task_list,
        "total_tasks": len(task_list)
    })

@app.route('/tasks/<string:id>',methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
        
    return jsonify({
            "message": "No task found."
        }), 404

if __name__ == '__main__':
    app.run(debug=True)