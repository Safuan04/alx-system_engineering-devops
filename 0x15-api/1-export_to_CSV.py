#!/usr/bin/python3
"""Impoering necesary modules"""
import csv
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
    for task in todos_json:
        TASK_COMPLETED_STATUS = task['completed']
        TASK_TITLE = task['title']
        data_to_add = [USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE]
        with open(f'{USER_ID}.csv', mode='a', newline='') as CSVfile:
            writer = csv.writer(CSVfile, delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(data_to_add)
