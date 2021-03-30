import json 
import csv

class json_csv:
    x = None
    def convert_json_csv(self, user_name, x):
        x = json.loads(x)
        file = csv.writer(open('data.csv', 'wb+'))
        file.writerow([user_name])
        