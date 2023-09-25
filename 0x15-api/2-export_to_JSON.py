#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress.
Extend the Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    emp_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    filename = "{}.json".format(emp_id)

    u = requests.get(user_url)
    t = requests.get(todos_url)

    user_dic = u.json()
    todo_dic = t.json()

    for user in user_dic:
        if user.get("id") == int(emp_id):
            USERNAME = user.get("username")
            break

    TASK_VALUE = []
    for todo in todo_dic:
        if todo.get("userId") == int(emp_id):
            TASK_VALUE.append(
                    {"task": todo.get("title"),
                        "completed": todo.get("completed"),
                        "username": USERNAME})

    TASK_KEY = {emp_id: TASK_VALUE}

    with open(filename, mode="w", encoding="utf-8") as wr_file:
        """dump to a file"""
        json.dump(TASK_KEY, wr_file)
