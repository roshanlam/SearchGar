from Crawler import *
from utils.checkSSL import checkForSSL

url_crawl = []

for url in url_crawl:
    if checkForSSL(url) == True:
        print("[*] Crawling")
    if checkForSSL(url) == False:
        print("No URl Given")