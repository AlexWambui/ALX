#!/usr/bin/python3
""" Fetches JSON data from an API """

import csv
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    user_todos = requests.get("{}/todos".format(user_url))
    user_todos = user_todos.json()
    file_name = user_id + ".json"
    dictionary = {}

    dictionary[user_id] = []

    for todo_task in user_todos:
        inner_dict = {}
        inner_dict["task"] = todo_task.get("title")
        inner_dict["completed"] = todo_task.get("completed")
        inner_dict["username"] = user_name
        dictionary.get(user_id).append(inner_dict)

    with open(file_name, 'w') as filename:
        json.dump(dictionary, filename)
