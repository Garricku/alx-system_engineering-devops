#!/usr/bin/python3
"""This is the 1-export_to_CSV module"""
import csv
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
        usr_name = user_data["username"]
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])

        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            for task in todos_data:
                emp_id = '{}'.format(employee_id)
                user_name = '{}'.format(usr_name)
                task_comp = '{}'.format(task["completed"])
                task_title = '{}'.format(task["title"])
                csv_writer.writerow([emp_id, user_name, task_comp, task_title])

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_todo_progress(employee_id)
