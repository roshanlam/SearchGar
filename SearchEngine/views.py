from django.shortcuts import render, redirect
from django.contrib import messages
import requests, pathlib
from bs4 import BeautifulSoup
import json
import requests
import re, os
from .search import startQuery

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def saveHistory(request):
    return render(request, 'savedHistory.html')

def crawlWebsite(request):
    if request.POST:
        websiteUrl = request.POST.get('WebsiteUrl')
        websiteName = request.POST.get('WebsiteName')
        website_info = crawl(websiteUrl, 5, websiteName)
        url = re.compile(r"https?://(www\.)?")
        saveInfo('Data', url.sub('', websiteUrl).strip().strip('/'), website_info)
        return render(request, 'submitWebsite.html', {'websiteName': websiteName, 'websiteUrl': websiteUrl})
    else:
        return render(request, 'submitWebsite.html')

def search(request):
    if request.POST:
        Query = request.POST.get('searchQuery')
        Result = startQuery(Query)
        return render(request, 'searchresults.html', {'Query': Query, 'Result': Result})
    else:
        return render(request, "home.html")

def crawl(url, depth, filename):
    try:
        response = requests.get(url, headers={'user-agent': 'code-monkey-search'})
    except:
        print('Failed to perform HTTP GET request on "%s"\n' % url)
        return
    website = BeautifulSoup(response.text, 'lxml')
    try:
        title = website.find('title').text
        paragraph = ''
        h1 = ''
        a = ''
        div = ''
        for tag in website.findAll():
            if tag.name == 'p':
                paragraph += tag.text.strip().replace('\n', '')
            if tag.name == 'h1':
                h1 += tag.text.strip().replace('\n', '')
            if tag.name == 'a':
                a += tag.text.strip().replace('\n', '')
            if tag.name == 'div':
                div += tag.text.strip().replace('\n', '')
    except:
        return
    result = {
        'url': url,
        'title': title,
        'paragraph': paragraph,
        'header1' : h1,
        'a': a,
        'div' : div
    }
    return result.values()


def saveInfo(folder, filename, info):
    try:
        folder = pathlib.Path("{}".format(folder))
        folder.mkdir(parents=True)
        filename = "{}.txt".format(filename)
        filepath = folder / filename
        folder = pathlib.Path("{}".format(folder))
        filename = "{}.txt".format(filename)
        filepath = folder / filename
        with filepath.open("w+") as f:
            f.write(str(info))
    except FileExistsError:
        folder = pathlib.Path("{}".format(folder))
        filename = "{}.txt".format(filename)
        filepath = folder / filename
        with filepath.open("w+") as f:
            f.write(str(info))
