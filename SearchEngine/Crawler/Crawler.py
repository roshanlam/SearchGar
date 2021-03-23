from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import parse_http_list, urlopen 
from urllib.error import HTTPError, URLError
from ordered_set import OrderedSet
from .crawler_helper import *

class Crawler:
    def __init__(self, url):
        self.crawled_urls = OrderedSet([])
        if(url_is_valid(url)):
            url = get_url(url, '')
            self.index = 0
            self.crawled_urls.add(url)
            self.crawl(url)
    
    def crawl(self, url):
        urls_found = []
        try:
            page = urlopen(url)
            content = page.read()
            soup = BeautifulSoup(content, 'lxml', parse_only=SoupStrainer('a'))
            for i in soup.find_all('a'):
                link = anchor.get('href')
                if url_is_valid(link):
                    link = get_clean_url(url, link)
                    if link_is_internal(link, url):
                        urls_found.append(link)
                else:
                    pass
                
        except HTTPError as e:
            pass 
        except URLError as e:
            pass 
        except Exception:
            pass