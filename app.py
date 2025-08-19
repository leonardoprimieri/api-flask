from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

task_control_id = 1
tasks = []

def find_task_by_id(task_id):
    for task in tasks:
        if task.id == task_id:
            return task

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_control_id
    data = request.get_json()
    new_task = Task(id=task_control_id,title=data['title'], description=data.get('description', ''))
    tasks.append(new_task)
    task_control_id += 1
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

@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task_by_id(task_id):
    task = find_task_by_id(task_id=task_id)
    if task:
        for task in tasks:
            if task.id == task_id:
                return jsonify(task.to_dict())
        
    return jsonify({
            "message": "No task found."
        }), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task_by_id(task_id):
    data = request.get_json()
    task = find_task_by_id(task_id=task_id)
    if task:
        if task.id == task_id:
            task.title = data.get('title', task.title)
            task.is_completed = data.get('is_completed', task.is_completed)
            task.description = data.get('description', task.description)
            return jsonify({"message": "Task successfully updated."})
        
    return jsonify({
        "message": "No task found."
    }), 404 

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    task = find_task_by_id(task_id=task_id)
    if task:
        tasks.remove(task)
        return jsonify({
            "message": "Task successfully deleted."
        })
    
    return jsonify({
        "message": "No task found."
    }), 404 


if __name__ == '__main__':
    app.run(debug=True, port=8000)