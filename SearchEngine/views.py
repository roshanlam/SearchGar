from django.shortcuts import render
from django.contrib import messages
import requests, pathlib
from bs4 import BeautifulSoup
import re
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def logout(request):
    return render('logout.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    return render(request, 'register.html')

def getInfo(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="lxml")
        metas = soup.find_all('meta')
        title = soup.find(['title', 'h1']).get_text()
        descrip = [meta.attrs['content'] for meta in metas if
                   'name' in meta.attrs and meta.attrs['name'] == 'description']
        if len(descrip) <= 0:
            descrip = [meta.attrs['content'] for meta in metas if
                       'name' in meta.attrs and meta.attrs['name'] == 'Description']
            info1 = soup.find(['p', 'a']).get_text()
        return title, descrip, info1

def saveInfo(folder, filename, info):
    try:
        folder = pathlib.Path("{}".format(folder))
        folder.mkdir(parents=True)
        filename = "{}.txt".format(filename)
        filepath = folder / filename
    except FileExistsError:
        folder = pathlib.Path("{}".format(folder))
        filename = "{}.txt".format(filename)
        filepath = folder / filename
    try:
        with filepath.open("a+", encoding="utf-8") as f:
            f.write(str(info))
    except FileExistsError:
        print("File {}".format(filename) + " already exists")

def crawlWebsite(request):
    if request.POST:
        websiteUrl = request.POST.get('WebsiteUrl')
        websiteName = request.POST.get('WebsiteName')
        website_info = getInfo(websiteUrl)
        url = re.compile(r"https?://(www\.)?")
        saveInfo('Data', url.sub('', websiteUrl).strip().strip('/'), website_info)
        return render(request, 'submitWebsite.html', {'websiteName': websiteName, 'websiteUrl': websiteUrl})
    else:
        return render(request, 'submitWebsite.html')

def search(request):
    if request.POST:
        return render(request, 'searchresults.html')
    else:
        messages.info(request, "Please check the spelling you have entered. ")
        return render(request, "home.html")

def settings(request):
    return render(request, 'settings.html')

def savedLinks(request):
    return render(request, 'savedLinks.html')

def savedHistory(request):
    return render(request, 'savedHistory.html')

def savedResult(request):
    return render(request, 'savedResult.html')

def gauth(request):
    pass
