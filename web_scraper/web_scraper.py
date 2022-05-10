import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Alba_(rabbit)"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="mw-body-content mw-content-ltr")
# print(results)
p_tags = results.find_all('p')
print(p_tags)


def get_citations_needed_count(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")