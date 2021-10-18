
"""
TODO: 1. finish the delete function
      2. Improve this HashMap and make it even faster and efficient
"""

class MyHashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in range(256)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key,value))

    def retrieve(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError

    def delete(self, key):
        pass