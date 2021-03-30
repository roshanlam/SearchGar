from django.shortcuts import render, HttpResponse, redirect
from django.http.response import HttpResponseRedirect
from django.core.exceptions import ValidationError, PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login as auth_login

from datetime import datetime 

ROOT_FOLDER_ID = "SI"
ROOT_FOLDER_NAME = "SearchIt"

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    return render('logout.html')

def gauth(request):
    pass

def search(request):
    if request.POST:
        return render(request, 'searchresults.html')
    else:
        return render(request, "home.html")
    
def settings(request):
    return render(request, 'settings.html')

def savedLinks(request):
    return render(request, 'savedLinks.html')

def savedHistory(request):
    return render(request, 'savedHistory.html')

def savedResult(request):
    return render(request, 'savedResult.html')