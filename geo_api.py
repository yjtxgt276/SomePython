#!/bin/env python3.6
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# google api
# my_srv_url = 'http://maps.googleapis.com/maps/api/geocode/json?'

#test api
my_srv_url = "http://py4e-data.dr-chuck.net/geojson?"
test_addr = "South Federal University"

while True:
    my_addr = input('Enter location: ')
    if len(my_addr) < 1:
        my_url = my_srv_url + urllib.parse.urlencode({'address': test_addr}) 
    else:
        my_url = my_srv_url + urllib.parse.urlencode({'address': my_addr})

    print('Retrieving', my_url)
    data = urllib.request.urlopen(my_url).read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        my_json = json.loads(data)
    except:
        my_json = None

    if not my_json or 'status' not in my_json or my_json['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    #print(json.dumps(my_json, indent=4))

    '''
    location = my_json['results'][0]['formatted_address']
    my_loc_id = my_json['results'][0]['place_id']
    print("location: ", location, "\nplace_id: ", my_loc_id)
    '''
    for result in my_json['results']:
        location = result['formatted_address']
        my_loc_id = result['place_id']
        print("location: ", location, "\nplace_id: ", my_loc_id)

