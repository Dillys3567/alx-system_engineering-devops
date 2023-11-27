#!/usr/bin/python3
""" Export data in json format
"""
import json
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
    name = user.get("username")
    data_json = {emp_id: []}
    for todo in todos:
        task = {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": name
                }
        data_json[emp_id].append(task)

    with open("{}.json".format(emp_id), "w") as jsonfile:
        json.dump(data_json, jsonfile)
