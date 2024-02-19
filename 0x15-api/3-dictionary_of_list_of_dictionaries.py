#!/usr/bin/python3
"""This is the 3-dictionary_of_list_of_dictionaries module"""
import requests
import json


def get_employee_todo_progress():
    """Returns information about his/her TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_employees_data = {}
        for user in users_data:
            employee_id = user["id"]
            employee_username = user["username"]

            todos_url = f"{base_url}/todos?userId={employee_id}"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            todo_list = []
            for task in todos_data:
                todo_list.append({
                    "username": employee_username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_employees_data[str(employee_id)] = todo_list

        json_filename = "todo_all_employees.json"
        with open(json_filename, "w") as jsonfile:
            json.dump(all_employees_data, jsonfile, indent=4)

        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_employee_todo_progress()
