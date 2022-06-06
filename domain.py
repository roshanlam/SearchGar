from urllib.parse import urlparse
import re

def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except Exception as e:
        return ''
    
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        return ''

def get_domain_name_without_extension(url):
    rex = "http(?:s)?:\/\/(?:www\.?)?(.+)"
    try:
        result = re.search(rex, url).groups()[0]
        return result.split('.')[0] + "-" + '-'.join(result.split('/')[1:])
    except Exception as e:
        return ''
    