import requests

BASE_URL = "http://127.0.0.1:8000"

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

def test_update_task():
    create_task_response = requests.post(f"{BASE_URL}/tasks", json=task_factory())
    create_task_response_json = create_task_response.json()
    created_task_id = create_task_response_json['id']

    update_task_response = requests.put(f"{BASE_URL}/tasks/{created_task_id}", json={
        "title": "Updated title"
    })

    update_task_response_json = update_task_response.json()

    assert update_task_response.status_code == 200
    assert update_task_response_json['message'] == 'Task successfully updated.'

    get_task_response = requests.get(f"{BASE_URL}/tasks/{created_task_id}")
    get_task_response_json = get_task_response.json()
    assert get_task_response_json['title'] == 'Updated title'

def test_delete_task():
    create_task_response = requests.post(f"{BASE_URL}/tasks", json=task_factory())
    create_task_response_json = create_task_response.json()
    created_task_id = create_task_response_json['id']

    delete_task_response = requests.delete(f"{BASE_URL}/tasks/{created_task_id}")

    delete_task_response_json = delete_task_response.json()

    assert delete_task_response.status_code == 200
    assert delete_task_response_json['message'] == 'Task successfully deleted.'

def test_delete_task_not_found():
    delete_task_response = requests.delete(f"{BASE_URL}/tasks/999999")
    assert delete_task_response.status_code == 404
    delete_task_response_json = delete_task_response.json()
    assert delete_task_response_json['message'] == 'No task found.'

def test_update_task_not_found():
    update_task_response = requests.put(f"{BASE_URL}/tasks/999999", json={
        "title": "Random"
    })
    update_task_response_json = update_task_response.json()

    assert update_task_response.status_code == 404
    assert update_task_response_json['message'] == 'No task found.'