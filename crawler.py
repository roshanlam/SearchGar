import re
import requests
from domain import *
from utils import *
from bs4 import BeautifulSoup
from mydb import MyDB

class Crawler:
    def __init__(self, url, depth):
        self.crawl(url, depth)
        
    def crawl(self, url, depth):
        if depth == 0:
            return
        self.download_url(url)
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            links = []
            for link in soup.find_all('a'):
                if link.get('href') is not None:
                    links.append(link.get('href'))
            for link in links:
                if re.match('http(?:s)?://', link) is None:
                    link = 'http://' + link
                self.crawl(link, depth - 1)
        except:
            pass

    def get_website_name(self, url):
        return get_domain_name(url).split('.')[0]

    def download_url(self, url):
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            text = soup.get_text()
            text = re.sub('\S*@\S*\s?', '', text)
            if not os.path.exists('Data'):
                os.makedirs('Data')
            website_name = self.get_website_name(url)
            if not os.path.exists('Data/' + website_name):
                os.makedirs('Data/' + website_name)
            with open('./Data/{}/{}content.txt'.format(self.get_website_name(url), get_domain_name_without_extension(url)), 'w') as f:
                f.write(text + '\n')
            db = MyDB()
            db.set(('./Data/{}/{}content.txt'.format(self.get_website_name(url), get_domain_name_without_extension(url))), url)
        except:
            pass
        
Crawler('http://www.google.com', 5)