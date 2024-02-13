import requests
from bs4 import BeautifulSoup

target_url = "https://news.ycombinator.com"
foundLinks = []

def make_request(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup



def crawl(url):
    links = make_request(url)
    for link in links.find_all('a'):
        found_link = link.get("href")
        if found_link and found_link.startswith('http'):
            print(found_link)
            foundLinks.append(found_link)


crawl(target_url)


