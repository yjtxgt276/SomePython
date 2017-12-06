#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved ", len(data)," characters")
root = ET.fromstring(data)
counts = root.findall(".//count")
result = 0
cnt = 0
for count in counts:
    cnt += 1
    result += int(count.text)

print("count:\t", cnt)
print("result:\t",result)



