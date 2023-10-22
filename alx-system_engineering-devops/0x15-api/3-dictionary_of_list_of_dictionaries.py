#!/usr/bin/python3
""" Fetches JSON data from an API """

import json
import requests


if __name__ == "__main__":
    user_url = "https://jsonplaceholder.typicode.com/users/"
    user_dictionary = requests.get(user_url).json()
    file_name = "todo_all_employees.json"
    dictionary = {}

    for todo_task in user_dictionary:
        name = todo_task.get("username")
        user_id = str(todo_task.get("id"))
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()
        dictionary[user_id] = []
        for data in user_data:
            inner_dictionary = {}
            inner_dictionary["username"] = name
            inner_dictionary["task"] = data.get("title")
            inner_dictionary["completed"] = data.get("completed")
            dictionary[user_id].append(inner_dictionary)

    with open(file_name, 'w') as filename:
        json.dump(dictionary, filename)
