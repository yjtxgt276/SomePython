import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1

for i in range(count):
    print("Retrieving: ", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos].get('href', None) 

print("The last url is: ", url)
print("The answer is: ", re.findall('known_by_(.*)\.html', url))
