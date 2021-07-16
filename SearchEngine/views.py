from django.shortcuts import render
import pathlib
from bs4 import BeautifulSoup
import requests
import re, os, glob, json
from .search import startQuery
from .lib import get_client_ip, saveQueryData, saveCrawlData, readFile, crawl, saveInfo
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.decorators import api_view

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def seeHistoryQuery(request):
    path = os.getcwd()
    ip_address = get_client_ip(request)
    # json_files = glob.glob(os.path.join(path, "*_search.json"))
    json_files = glob.glob(os.path.join(path, ip_address + "_search.json"))
    for j in json_files:
        data = j
    try:
       rf = readFile(data)
    except:
        pass
    return HttpResponse(rf, content_type='application/json')

def seeHistoryCrawl(request):
    path = os.getcwd()
    ip_address = get_client_ip(request)
    # json_files = glob.glob(os.path.join(path, "*_crawl.json"))
    json_files = glob.glob(os.path.join(path, ip_address + "_crawl.json"))
    for j in json_files:
        data = j
    try:
       rf = readFile(data)
    except:
        pass
    return HttpResponse(rf, content_type='application/json')

def crawlWebsite(request):
    if request.POST:
        websiteUrl = request.POST.get('WebsiteUrl')
        websiteName = request.POST.get('WebsiteName')
        website_info = crawl(websiteUrl, websiteName)
        url = re.compile(r"https?://(www\.)?")
        ip_add = get_client_ip(request)
        saveCrawlData(websiteUrl, websiteName, ip_add)
        saveInfo('Data', url.sub('', websiteUrl).strip().strip('/'), website_info)
        return render(request, 'submitWebsite.html', {'websiteName': websiteName, 'websiteUrl': websiteUrl})
    else:
        return render(request, 'submitWebsite.html')

@api_view(['GET', 'POST'])
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
