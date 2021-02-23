from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.forms import EmailField
from django.core.exceptions import ValidationError
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'signup.html')

#@login_required
def home(request):
    return render(request, 'home.html')

def user_signup(request):
    return render(request, 'signup.html')

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
    pass

def settings(request):
    return render(request, 'settings.html')

def savedLinks(request):
    pass

def savedHistory(request):
    pass

def savedResult(request):
    pass

def addWebsite(request):
    pass

def removeWebsite(request):
    pass

def updateWebsite(request):
    pass

def isEmailAddressValid(email):
    try:
        EmailField().clean(email)
        return True
    except ValidationError:
        return False