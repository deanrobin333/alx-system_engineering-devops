#!/usr/bin/python3
# 3-dictionary_of_list_of_dictionaries.py

'''script to export data in the JSON format fetched from an api
from all employes
'''

import json
import requests

web_url = 'https://jsonplaceholder.typicode.com'


def export_csv2():
    '''function that exports data in json for everyone'''

    # get users info e.g https://jsonplaceholder.typicode.com/users
    users_url = '{}/users'.format(web_url)

    # get info from api
    response = requests.get(users_url)
    # pull data from api
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)

    # extract users data
    builder = {}
    for user in data:
        user_id = user.get('id')
        # print("id is: {}".format(user_id))

        user_name = user.get('username')
        # print("username is: {}".format(user_name))

        dict_key = str(user_id)
        # print("dict_key: {}".format(dict_key))

        builder[dict_key] = []
        # get user info about todo tasks
        # e.g https://jsonplaceholder.typicode.com/users/1/todos
        tasks_url = '{}/todos?userId={}'.format(web_url, user_id)
        # print("tasks url is: {}".format(tasks_url))

        # get info from api
        response = requests.get(tasks_url)
        # pull data from api
        tasks = response.text
        # parse the data into JSON format
        tasks = json.loads(tasks)
        # print("JSOON LOADS IS: {}".format(tasks))

        for task in tasks:
            json_data = {
                "task": task['title'],  # or use get method
                "completed": task['completed'],
                "username": user_name
            }
            # append dictionary key to the dictionary
            builder[dict_key].append(json_data)
    # write the data to the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)


if __name__ == ('__main__'):
    export_csv2()
