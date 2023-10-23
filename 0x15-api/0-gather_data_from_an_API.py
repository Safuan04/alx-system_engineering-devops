#!/usr/bin/python3
"""Importing necessary modules"""
import requests
from sys import argv


if __name__ == "__main__":

    employee_id = argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    req_user = requests.get(user_url)
    json_user = req_user.json()
    EMPLOYEE_NAME = json_user.get('name')

    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    todos_params = {'userId': employee_id}
    todos_req = requests.get(todos_url, params=todos_params)
    todos_json = todos_req.json()

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    for task in todos_json:
        if task['completed'] is True:
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1

    print(f"Employee {EMPLOYEE_NAME} is done with tasks"
          f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for task in todos_json:
        if task['completed'] is True:
            TASK_TITLE = f"\t {task['title']}"
            print(TASK_TITLE)

