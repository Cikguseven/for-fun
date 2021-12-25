import requests
from bs4 import BeautifulSoup

links = open('links.txt', 'r').read().splitlines()

for url in links:
    if not url.isspace():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='mh-mobile')
        review_elements = results.find('div', class_='entry clearfix')
        z = review_elements.getText()
        keyword = 'TheRantingPanda'
        index = z.find(keyword)
        print(z[index:index + 170])
        print()
