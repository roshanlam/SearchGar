import os
import json
        
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

def delete_file_contents(path):
    open(path, 'w').close()
    
def file_to_set(file_name):
    results = set()
    try:
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
    except FileNotFoundError:
        return "File not found"
    return results

def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l + '\n')

class JSONValidator:
    def __init__(self, data):
        self.data = data
    
    def validate(self):
        if type(self.data) is not dict:
            return False
        return True

class CRUDJson:
    def __init__(self, path, data):
        self.path = path
        self.data = data
    
    def write_json_file(self):
        validator = JSONValidator(self.data)
        if not validator.validate():
            return "Make sure the data is valid."
        else:
            with open(self.path, 'w') as f:
                f.write(json.dumps(self.data, indent=4))
                
    def read_json_file(self):
        with open(self.path) as f:
            try:
                read_data = json.load(f)
            except ValueError:
                return "Make sure the data is valid."
        return read_data

    def update_json_file(self):
        validator = JSONValidator(self.data)
        if not validator.validate():
            return "Make sure the data is valid."
        else:
            with open(self.path, 'r') as f:
                try:
                    old_data = json.load(f)
                except ValueError:
                    return "Make sure the data is valid."
                old_data.update(self.data)
            with open(self.path, 'w') as f:
                f.write(json.dumps(self.data, indent=4))
                
    def delete_json_file_contents(self):
        open(self.path, 'w').close()

    def delete_json_file(self):
        if os.path.exists(self.path):
            os.remove(self.path)