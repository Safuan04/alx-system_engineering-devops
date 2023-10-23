#!/usr/bin/python3
"""Importing necessary modules"""
import json
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

    USER_ID = employee_id
    USERNAME = json_user.get('username')
    employee_dict = {}
    list_attr = []
    for task in todos_json:
        TASK_COMPLETED_STATUS = task['completed']
        TASK_TITLE = task['title']

        employee_attr = {}
        employee_attr['task'] = TASK_TITLE
        employee_attr['completed'] = TASK_COMPLETED_STATUS
        employee_attr['username'] = USERNAME
        list_attr.append(employee_attr)

    employee_dict[USER_ID] = list_attr

    with open(f'{USER_ID}.json', mode="w", encoding="UTF-8") as JsonFile:
        json.dump(employee_dict, JsonFile)
