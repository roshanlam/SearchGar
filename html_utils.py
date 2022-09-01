import re
import urllib
from bs4 import BeautifulSoup

# clean html code and turn it into plain text for processing
def clean_html(html):
    soup = BeautifulSoup(html)
    return soup.get_text()

def get_links(html):
    soup = BeautifulSoup(html)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

def get_title(html):
    soup = BeautifulSoup(html)
    return soup.title.string

def get_images(html):
    soup = BeautifulSoup(html)
    images = []
    for image in soup.find_all('img'):
        images.append(image.get('src'))
    return images
