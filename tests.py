import pytest
import requests

BASE_URL = "http://127.0.0.1:8000"
tasks = []

def test_create_task():
    new_task = {
        "title": "Task title",
        "description": "Task description",
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task)
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response
    assert "is_completed" in json_response
    assert "id" in json_response
    assert "description" in json_response

