#!/usr/bin/python3
# 2-export_to_JSON.py

'''script to export data in the JSON format fetched from an api'''

import json
import requests
from sys import argv

web_url = 'https://jsonplaceholder.typicode.com'


def export_json():
    '''function that exports data to JSON format'''

    user_id = argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(web_url, user_id)
    # print("user url is: {}".format(user_url))

    # get info from api
    response = requests.get(user_url)
    # pull data from api
    data = response.text
    # parse the data into JSON format
    data = json.loads(data)
    # extract user data, in this case, username of employee
    user_name = data[0].get('username')
    # print("id is: {}".format(user_id))
    # print("username is: {}".format(user_name))

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

    dict_key = str(user_id)
    # print("dict_key: {}".format(dict_key))

    # build the json
    builder = {dict_key: []}
    for task in tasks:
        json_data = {
            "task": task['title'],  # or use get method
            "completed": task['completed'],
            "username": user_name
        }
        # append dictionary key to the dictionary
        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)


if __name__ == ('__main__'):
    export_json()
