import requests
from bs4 import BeautifulSoup
class Crawler(object):
    results = []
    def crawl(self, url):
        try:
            res = requests.get(url)
        except:
            return
        content = BeautifulSoup(res.text, 'lxml')
        try:
            title = content.find('title').text
            website_description = ''
        except:
            return
