#!/usr/bin/python3
""" Export user data into csv
"""
import csv
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
    name = user.get("name")
    with open("{}.csv".format(emp_id), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([emp_id, name, todo.get(
                "completed"), todo.get("title")])
