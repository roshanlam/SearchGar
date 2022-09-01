import redis

from utils import dict_vals_to_string

class MyDB(object):
    def __init__(self):
        self.db = redis.Redis(host='localhost', port=6379, db=0)

    def get(self, key):
        got_value = self.db.get(key)
        return got_value
    
    def set(self, key, value):
        self.db.set(key, value)
        
    def delete(self, key):
        deleted_value = self.db.delete(key)

    def delete_all(self):
        self.db.flushdb()
        
    def keyexists(self, key):
        return True if self.db.exists(key) else False
    
    def get_urls(self):
        return self.db.keys()
    
    def store_website_data(self, url, content):
        url, content = dict_vals_to_string(url, content)
        self.set(url, content)
        return True if self.keyexists(url) else False