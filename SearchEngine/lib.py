from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json, codecs

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

class JsonEncoder(DjangoJSONEncoder):
    def __init__(self, o):
        if isinstance(o):
            return o
        return super().default(o)