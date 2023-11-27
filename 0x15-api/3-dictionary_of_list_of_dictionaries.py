#!/usr/bin/python3
"""put all user data into a json file
"""
import json
import requests

def fetch_users_data():
    """ fetch all user data
    """
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    json_data = {}
    for user in users:
        emp_id = user["id"]
        todos = requests.get(url + f"todos?userId={emp_id}").json()
        json_data[emp_id] = []
        for todo in todos:
            task = {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                    }
            json_data[emp_id].append(task)
    return json_data

if __name__ == "__main__":
    json_data = fetch_users_data()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_data, jsonfile)
