#!/usr/bin/python3
"""This is the 2-export_to_JSON module"""
import json
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """Returns information about his/her TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        employee_username = user_data["username"]

        todo_list = []
        for task in todos_data:
            todo_list.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_username
            })

        employee_data = {str(employee_id): todo_list}

        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as jsonfile:
            json.dump(employee_data, jsonfile, indent=4)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_todo_progress(employee_id)
