import requests
from bs4 import BeautifulSoup

# url
url = "https://www.w3schools.com/"

# headers to mimic the browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# send request
response = requests.get(url, headers=headers)

# parse html content
soup = BeautifulSoup(response.text, "html.parser")

# find all section heading (eg, h1, h2, h3), etc
# with tag name
headings = soup.find_all(['h1', 'h2', 'h3'])

# with class name
# soup.find_all("a", class_="w3-bar-item")

# print extracted headings
for heading in headings:
    print(heading.text.strip())

# to handle the dynamic or interactive data scrapping use selenium instead requests