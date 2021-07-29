from django.shortcuts import render
import pathlib
from bs4 import BeautifulSoup
import requests
import re, os, glob, json
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
import jwt
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .search import startQuery
from .lib import get_client_ip, saveQueryData, saveCrawlData, readFile, crawl, saveInfo
from .models import User
from .serializers import UserSerializer

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

def search(request):
    query = ''
    if request.method == 'POST':
        query = request.POST.get("searchquery", "")
        ip_address = get_client_ip(request)
        saveQueryData(query, ip_address)
        Result = startQuery(query)
        Result = os.path.splitext(Result)[0]
        Result = "https://" + Result
        return JsonResponse({'Result': Result})
    else:
        return JsonResponse({'Result': 'None'})
    """
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
    """

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        key = "secret"
        token = jwt.encode(payload, key, algorithm="HS256")
        response = Response()
        response.set_cookie(key="JWT", value=token, httponly=True)
        response.data = {"JWT": token}
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('JWT')
        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token, 'secret', algorithums=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSeriallizer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('JWT')
        response.data = {"message":"success"}
        return response