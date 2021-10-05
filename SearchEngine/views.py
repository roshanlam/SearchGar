from django.shortcuts import render
from bs4 import BeautifulSoup
import re, os, glob, json, requests, pathlib
from django.http import JsonResponse, HttpResponse
import datetime, jwt
from rest_framework import generics, status, permissions, viewsets
from .search import startQuery
from .lib import get_client_ip, saveQueryData, saveCrawlData, readFile, crawl, saveInfo

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def seeHistoryQuery(request):
    path = os.getcwd()
    ip_address = get_client_ip(request)
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

from .query import *

def search(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get("searchquery", "")
        ip_address = get_client_ip(request)
        saveQueryData(query, ip_address)
        #q = Query()
        #Result = q.free_text_query(query)
        Result = startQuery(query)
        Result = os.path.splitext(Result)[0]
        Result = "https://" + Result
        return JsonResponse({'Result': Result})
        #return render(request, 'searchresults.html', {'Query': Query, 'Result': Result})
    else:
        return render(request, 'home.html')
        #return JsonResponse({'Result': 'None'})