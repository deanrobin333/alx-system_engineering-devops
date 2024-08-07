#!/usr/bin/python3
# 1-export_to_CSV.py

'''script to export data in the CSV format fetched from an api'''

import json
import requests
from sys import argv

web_url = 'https://jsonplaceholder.typicode.com'


def export_csv():
    '''function that exports employee information to csv'''

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
    # print("name is: {}".format(user_name))

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

    # build the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)


if __name__ == ('__main__'):
    export_csv()
