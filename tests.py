import requests

BASE_URL = "http://127.0.0.1:8000"
tasks = []

def task_factory():
    return  {
        "title": "Task title",
        "description": "Task description",
    }

def test_create_task():
    create_task_response = requests.post(f"{BASE_URL}/tasks", json=task_factory())
    create_task_response_json = create_task_response.json()

    assert create_task_response.status_code == 200
    assert "id" in create_task_response_json
    assert "is_completed" in create_task_response_json
    assert "title" in create_task_response_json
    assert "description" in create_task_response_json

def test_read_tasks():
    requests.post(f"{BASE_URL}/tasks", json=task_factory())

    get_tasks_response = requests.get(f"{BASE_URL}/tasks")
    get_tasks_response_json = get_tasks_response.json()

    assert get_tasks_response.status_code == 200
    assert get_tasks_response_json['total_tasks'] > 0

