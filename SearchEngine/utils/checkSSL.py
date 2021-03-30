import requests

def checkForSSL(url):
    res = requests.get(url, verify=True)
    if res.status_code == 200:
        return True
    elif res.status_code != 200:
        return False
    elif len(url) <= 0:
        return False