#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress.
"""
import requests
from sys import argv


def get_employee_info():
    """" returns information about his/her TODO list progress. """

    emp_id = int(argv[1])
    url_1 = "https://jsonplaceholder.typicode.com/todos/"
    url_2 = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todo_response = requests.get(url_1).json()
    user_response = requests.get(url_2).json()

    task_done = 0
    total_task = 0
    task_title = ""
    Employee_name = user_response["name"]

    for response in todo_response:
        if response["userId"] is emp_id:
            if response["completed"] is True:
                task_done += 1
                task_title += f"\t {response['title']}\n"
            total_task += 1

    print(f"""Employee {Employee_name} is done \
with tasks({task_done}/{total_task}):
{task_title}""", end="")


if __name__ == '__main__':
    get_employee_info()
