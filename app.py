from flask import Flask, request
from models.task import Task

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks.append(data)
    return tasks

if __name__ == '__main__':
    app.run(debug=True)