import requests
import re
from bs4 import BeautifulSoup


# URL = "https://en.wikipedia.org/wiki/Audio_system_measurements"
URL = "https://en.wikipedia.org/wiki/Alba_(rabbit)"
page = requests.get(URL)

# soup = BeautifulSoup(page.content, "html.parser")
#
# results = soup.find('title', 'Wikipedia:Citation needed')
# print(results)
# p_tags = results.find_all('p')
# print(soup.find_all(title='Wikipedia:Citation needed'))
print("""
    **** Wikipedia Citation Needed finder! ****
    ** Enter a complete Wikipedia URL to    **
    ** to receive a nicely formatted string **  
    ** of any citations that article needs  **  
    ******************************************
""")
URL = input("Enter a full wikipedia URL > ")


def get_citations_needed_count(url):
    citation_count = 0
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    citation_needed = soup.find_all(title='Wikipedia:Citation needed')
    for needed in citation_needed:
        citation_count += 1

    print(f'** The Wikipedia page at url: {url} needs {citation_count} citations **')


def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    citation_needed = soup.find_all(title='Wikipedia:Citation needed')
    print("** The following lines require citation **")
    for needed in citation_needed:
        content = str(needed.parent.parent.parent)
        pattern = r"<[^<>]+>"
        parsed_content = re.sub(pattern, '', content)
        print(parsed_content)


get_citations_needed_count(URL)


get_citations_needed_report(URL)
