import json
import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import pandas as pd
from rich.console import Console

class Crawler():
    def __init__(self):
        self.search_results = []

def crawl(url, depth):
    try:
        console = Console()
        console.print('[bold blue]Crawling url: [bold white]"%s" at depth: [yellow]%d' % (url, depth))
        response = requests.get(url, headers={'user-agent': 'code-monkey-search'})
    except:
        print('Failed to perform HTTP GET request on "%s"\n' % url)
        return
    website = BeautifulSoup(response.text, 'lxml')
    try:
        title = website.find('title').text
        paragraph = ''
        h1  = ''
        a = ''
        for tag in website.findAll():
            if tag.name == 'p':
                paragraph += tag.text.strip().replace('\n', '')
            if tag.name == 'h1':
                h1 += tag.text.strip().replace('\n', '')
            if tag.name == 'a':
                a += tag.text.strip().replace('\n', '')
    except:
        return
    result = {
        'url': url,
        'title': title,
        'paragraph': paragraph,
        'header1' : h1,
        'a': a
    }
    with open('data.csv', 'a+') as f:
        w = csv.writer(f)
        for k, v in result.items():
            w.writerow([k, v])

    if depth == 0:
        return
    links = website.findAll('a')

    for link in links:
        try:
            if 'https' in link['href']:
                crawl(link['href'], depth - 1)
        except KeyError:
            pass


def duplicate_check(file):
    try:
        data = pd.read_csv(file)
        infoToSave = data.drop_duplicates(keep='last')
        df = pd.DataFrame(infoToSave)
        df.to_csv(file)
    except:
        return "Failed"
    return "Success"

#for i in range(2):
#    websites = ['https://www.geeksforgeeks.org', 'https://www.mayoclinic.org/']
#    crawl(websites[i], 5)
#df_csv = pd.read_csv('data.csv')
duplicate_check('data.csv')
