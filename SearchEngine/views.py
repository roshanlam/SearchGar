from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'signup.html')
def home(request):
    return render(request, 'home.html')