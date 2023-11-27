#!/usr/bin/python3
""" Gather data for an employee from a REST ap
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    resp = requests.get(url + "users/{}".format(emp_id))
    user = resp.json()
    params = {"userId": emp_id}
    todo_resp = requests.get(url + "todos", params=params)
    todos = todo_resp.json()
    completed = []
    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for todo in completed:
        print("\t {}".format(todo))
