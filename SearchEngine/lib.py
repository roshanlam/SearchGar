from datetime import datetime
import csv, json
import pandas as pd

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def saveQueryData(query, ip_address):
    fields = ['query', 'time']
    now = datetime.now()
    rows = [[query], [now.strftime("%d/%m/%Y %H:%M:%S")]]
    filename = ip_address
    with open(filename + '_search' + '.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

def saveCrawlData(url, website_name, ip_address):
    fields = ['url', 'website_name', 'date']
    now = datetime.now()
    rows = [[url],[website_name], [now.strftime("%d/%m/%Y %H:%M:%S")]]
    filename = ip_address
    with open(filename + '_crawl' + '.csv', 'a+') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        writer.writerows(rows)

def csvToJson(csvFile, JsonFile):
    data = {}
    with open(csvFile) as CFile:
        Reader = csv.DictReader(CFile)
        for r in Reader:
            query = r['query']
            data[query] = r
            time = r['time']
            data[time] = r

    with open(JsonFile, 'w') as JFile:
        JFile.write(json.dumps(data, indent=4))
