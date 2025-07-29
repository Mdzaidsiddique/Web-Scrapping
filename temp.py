import requests
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/"

# send http request
response = requests.get(url)

# parse all html content
soup = BeautifulSoup(response.text, "html.parser")

# get all h2 tags with class title

titles = soup.find_all("h2")

print(type(titles)) # <class 'bs4.element.ResultSet'>

# print the
for title in titles:
    print(title.text.strip())