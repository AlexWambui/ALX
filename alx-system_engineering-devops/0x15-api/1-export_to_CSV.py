#!/usr/bin/python3
""" Fetches JSON data from an API """

import csv
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user_id
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    user_todos = requests.get("{}/todos".format(user_url))
    user_todos = user_todos.json()
    file_name = user_id + ".csv"

    with open(file_name, 'w') as csvfile:
        for item in user_todos:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                item.get("userId"), user_name, item.get("completed"),
                item.get("title")))
