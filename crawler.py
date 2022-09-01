import re
import requests
from domain import *
from utils import *
from bs4 import BeautifulSoup
from mydb import MyDB
import re

from crawlerlib import CrawlerLib
from domain import get_domain_name, get_domain_name_without_extension
from crawleradvanced import Crawler as SmartCrawler

class Crawler:
    def __init__(self, url):
        self.url = url
        self.domain = get_domain_name(url)
        self.domain_without_extension = get_domain_name_without_extension(url)
        self.db = MyDB()
        self.crawlerlib = CrawlerLib()

    def classify_website(self):
        smartcrawler = SmartCrawler(self.url)
        result = smartcrawler.classify()
        smartcrawler.save()
        return result

    def crawl(self):
        """
        Crawl the website and store the data in the database
        """
        website_data = self.crawlerlib.get_website_data(self.url)
        website_data["category"] = self.classify_website()
        self.db.store_website_data(self.url, website_data)
        links = self.crawlerlib.gather_links(self.url)
        for link in links:
            if link.startswith("http"):
                crawler = Crawler(link)
                crawler.crawl()
            else:
                link = "http://" + self.domain + link
                crawler = Crawler(link)
                crawler.crawl()
        return website_data

Crawler('https://www.google.com').crawl()