#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress.
"""
import csv
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
    Employee_name = user_response["username"]
    file_name = f"{user_response['id']}.csv"

    user_data = []
    for response in todo_response:
        if response["userId"] is emp_id:
            data = [
                response['userId'],
                Employee_name,
                response['completed'],
                response['title']
            ]
            user_data.append(data)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for row in user_data:
            writer.writerow(row)


if __name__ == '__main__':
    get_employee_info()
