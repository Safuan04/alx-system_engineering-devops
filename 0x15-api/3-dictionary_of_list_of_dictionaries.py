#!/usr/bin/python3
"""Importing necessary modules"""
import json
import requests


if __name__ == "__main__":

    all_empls = requests.get("https://jsonplaceholder.typicode.com/users")
    all_empls_json = all_empls.json()
    employee_dict = {}

    for employee in all_empls_json:
        USER_ID = employee.get('id')
        user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
        req_user = requests.get(user_url)
        json_user = req_user.json()
        USERNAME = json_user.get('username')

        todos_url = 'https://jsonplaceholder.typicode.com/todos'
        todos_params = {'userId': USER_ID}
        todos_req = requests.get(todos_url, params=todos_params)
        todos_json = todos_req.json()

        list_attr = []

        for tasks in todos_json:
            TASK_COMPLETED_STATUS = tasks['completed']
            TASK_TITLE = tasks['title']

            employee_attr = {}
            employee_attr['username'] = USERNAME
            employee_attr['task'] = TASK_TITLE
            employee_attr['completed'] = TASK_COMPLETED_STATUS
            list_attr.append(employee_attr)

            employee_dict[USER_ID] = list_attr

    with open('todo_all_employees.json', mode="w", encoding="UTF-8") as JFile:
        json.dump(employee_dict, JFile)
