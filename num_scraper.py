from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "http://py4e-data.dr-chuck.net/comments_42.html"
url = "http://py4e-data.dr-chuck.net/comments_47168.html"

html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
    # Look at the parts of a tag
    sum += int(tag.contents[0])

print(sum)
