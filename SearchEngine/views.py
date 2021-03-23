from django.db.models import query
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.forms import EmailField
from django.core.exceptions import ValidationError, PermissionDenied
from django.http import Http404
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from .models import WebsiteList

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'signup.html')

#@login_required
def home(request):
  #  if permissions.is_authenticated(request.user):
        return render(request, "home.html") #, content={"user": request.user})
  #  return redirect('rest_framework:login')

class WebsiteList(APIView):

    permission_classes = (permissions.IsAuthenticated)
    def get(self, request, format=None):
        website_lists = WebsiteList.objects.filter(owner=request.user)
        serializer = WebsiteSerializer(website_lists, many=True)
        return Response(serializer.data)
    def post(self, reqest, format=None):
        serializers = WebsiteListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)


def user_signup(request):
    return render(request, 'signup.html')

def user_google_login(request):
    pass
def user_login(request):
   return render(request, 'login.html')

#@login_required
def adminHome(request):
    return render(request, 'adminHome.html')

def logout(request):
    return render(request, 'logout.html')

def adminLogin(request):
    return render(request, 'adminLogin.html')

def search(request):
    if request.POST:
        return render(request, 'searchresult.html')
    else: 
        return render(request, 'home.html')

def settings(request):
    return render(request, 'settings.html')

def savedLinks(request):
    pass

def savedHistory(request):
    pass

def savedResult(request):
    pass

def addWebsite(request):
    websites = WebsiteList.objects.all() 
    if request.method == 'POST':
            if 'websiteAdd' in request.POST:
                title = request.POST["title"] #title
                url = request.POST['url']
                Website = WebsiteList(title=title, url=url)
                Website.save() #saving the todo 
                return redirect('/')
            if "taskDelete" in request.POST: #checking if there is a request to delete a todo
                checkedlist = request.POST["checkedbox"] #checked todos to be deleted
                for website in checkedlist:
                    website = WebsiteList.objects.get(id=int(website)) #getting todo id
                    website.delete() #deleting todo
            return render(request, 'addWebsite.html', {"website": website})

def removeWebsite(request):
    return render(request, 'removeWebsite.html')

def updateWebsite(request):
    pass



def isEmailAddressValid(email):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False