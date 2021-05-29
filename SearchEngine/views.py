from django.shortcuts import render
import pathlib
from bs4 import BeautifulSoup
import requests
import re, os, glob, json
from .search import startQuery
from .lib import get_client_ip, saveQueryData, saveCrawlData, readFile
from django.http import JsonResponse
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def seeHistoryQuery(request):
    path = os.getcwd()
    json_files = glob.glob(os.path.join(path, "*_search.json"))
    for j in json_files:
        data = j
    try:
       rf = readFile(data)
    except:
        pass
    #return JsonResponse({'History': rf}, safe=False)
    return HttpResponse(rf, content_type='application/json')

def seeHistoryCrawl(request):
    path = os.getcwd()
    json_files = glob.glob(os.path.join(path, "*_crawl.json"))
    for j in json_files:
        data = j
    try:
       rf = readFile(data)
    except:
        pass
    #return JsonResponse({'History': rf}, safe=False)
    return HttpResponse(rf, content_type='application/json')
def crawlWebsite(request):
    if request.POST:
        websiteUrl = request.POST.get('WebsiteUrl')
        websiteName = request.POST.get('WebsiteName')
        website_info = crawl(websiteUrl, 3, websiteName)
        url = re.compile(r"https?://(www\.)?")
        ip_add = get_client_ip(request)
        saveCrawlData(websiteUrl, websiteName, ip_add)
        saveInfo('Data', url.sub('', websiteUrl).strip().strip('/'), website_info)
        return render(request, 'submitWebsite.html', {'websiteName': websiteName, 'websiteUrl': websiteUrl})
    else:
        return render(request, 'submitWebsite.html')

def search(request):
    if request.POST:
        Query = request.POST.get('searchQuery')
        ip_add = get_client_ip(request)
        saveQueryData(Query, ip_add)
        Result = startQuery(Query)
        Result = os.path.splitext(Result)[0]
        Result = "https://" + Result
        return render(request, 'searchresults.html', {'Query': Query, 'Result': Result})
    else:
        return render(request, "home.html")

def crawl(url, depth, filename):
    try:
        response = requests.get(url)
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
