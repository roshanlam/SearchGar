from django.shortcuts import render
from bs4 import BeautifulSoup
import re, os, glob, json, requests, pathlib
from django.http import JsonResponse, HttpResponse
import datetime, jwt
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.utils.safestring import mark_safe
from rest_framework import generics, status, permissions, viewsets

from .forms import CustomUserCreationForm
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


def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'{form.cleaned_data["email"]} registered successfully!')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, mark_safe(f'You are already logged in as <b>{request.user.username}</b>. To switch user'
                                         f' <a href="#" data-toggle="modal" data-target="#logoutModal"></i>'
                                         f'log out here.</a>'))
        return redirect('index')

    username = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            messages.success(request, f'User {user.username} logged in successfully!')
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('index')
        else:
            messages.warning(request, 'Could not authenticate, check credentials.')

    return render(request, 'login.html', context = {"username": username})


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')