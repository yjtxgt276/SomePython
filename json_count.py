#!/bin/env python3.6
import json
import urllib.request

test_url = "http://py4e-data.dr-chuck.net/comments_42.json"
while True:
    my_url = input("Enter the url:")
    print(my_url)
    if my_url == "":
        #my_data = urllib.request.urlopen(test_url).read().decode()
        my_data = urllib.request.urlopen(test_url).read()
    else:
        my_data = urllib.request.urlopen(my_url).read().decode()

    my_json = json.loads(my_data)
    print(type(my_json), '\n', my_json)
    if 'comments' not in my_json:
        print("No comments found")
        continue

    sum = 0 
    for comment in my_json['comments']:
        sum += comment['count']

    print(sum)
