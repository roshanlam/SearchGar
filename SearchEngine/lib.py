from datetime import datetime
import json, codecs, requests
from bs4 import BeautifulSoup
import pathlib

def crawl(url, filename):
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        print('Failed to perform HTTP GET request on "%s"\n' % url)
        return
    website = BeautifulSoup(response.text, 'lxml')
    try:
        title = website.find('title').text
        paragraph = ''
        h1 = ''
        h2 = ''
        h3 = ''
        a = ''
        div = ''
        for tag in website.findAll():
            if tag.name == 'p':
                paragraph += tag.text.strip().replace('\n', '')
            if tag.name == 'h1':
                h1 += tag.text.strip().replace('\n', '')
            if tag.name == 'h2':
                h2 += tag.text.strip().replace('\n', '')
            if tag.name == 'h3':
                h3 += tag.text.strip().replace('\n', '')

            if tag.name == 'a':
                a += tag.text.strip().replace('\n', '')
            if tag.name == 'div':
                div += tag.text.strip().replace('\n', '')
        result = {
            'url': url,
            'title': title,
            'paragraph': paragraph,
            'header1': h1,
            'header2': h2,
            'header3': h3,
            'a': a,
            'div': div
        }
    except ValueError:
        if len(result) == 0:
            raise ValueError('Crawl info is empty')
        else:
            raise ValueError('Something is wrong, it is related to value error')
    return result.values()

def saveInfo(folder, filename, info):
    try:
        folder = pathlib.Path("{}".format(folder))
        folder.mkdir(parents=True)
        filename = "{}.txt".format(filename)
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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def saveQueryData(query, ip_address):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = ip_address
    with open(filename + '_search' + '.json', 'a+') as f:
        data = {
            ip_address: [{
                'Query': query,
                'Time': time
            }]
        }
        json.dump(data, f, indent=4, sort_keys=True)

def saveCrawlData(url, website_name, ip_address):
    now = datetime.now()
    time = now.strftime("%d/%m/%Y %H:%M:%S")
    filename = ip_address
    with open(filename + '_crawl' + '.json', 'a+') as f:
        data = {
            ip_address: [{
                'Website Url': url,
                'Website Name': website_name,
                'Time': time
            }]
        }
        json.dump(data, f, indent=4, sort_keys=True)

def readFile(path, encoding='utf-8'):
    with codecs.open(path, 'r', encoding=encoding) as f:
        try:
            content = f.read()
        except UnicodeDecodeError as e:
            raise Exception("%s: %s" % (e, path))
    return content

