from urllib.request import urlopen
#from link_finder import LinkFinder
from domain import *
#from general import *

class Spider(object):
    allowed_domains = ['.com', '.org', '.gov', '.edu']
    website_name = ''
    main_url = ''
    domain_name = ''
    to_crawl_file = ''
    crawled_file = ''
    to_crawl = set()
    crawled = set()
    def __init__(self, website_name, main_url, domain_name):
        Spider.website_name = website_name
        self.handles = {}

    def parse(self, reponse):
        pass
