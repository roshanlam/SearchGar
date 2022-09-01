from datetime import datetime
from enum import IntEnum
import json
import os

from utils import JSONValidator

from dataclasses import dataclass

class status(IntEnum):
    RUNNING = 1
    FAIL = 2
    STALE = 0

@dataclass
class Logger(object):
    name: str
    status: status
    start_time: datetime
    end_time: datetime
    file_name: str
    date: datetime
    
    def __init__(self, name):
        self.date = datetime.now()
        self.status = status.STALE
        self.name = name
        self.start_time = datetime.today().strftime('%d%H%M%S%f')
        self.file_name = './Data/logger/' + self.name + '_status.json'

    def start(self):
        if self.status is status.RUNNING:
            raise Exception('Already running')
        self.status = status.RUNNING
        
    def end(self, status):
        if not self.status is status.RUNNING:
            raise Exception('Not running')
        if not os.path.exists('Data'): 
            os.makedirs('Data')
        if not os.path.exists('./Data/logger'):
            os.makedirs('./Data/logger')
        self.end_time = datetime.today().strftime('%d%H%M%S%f')
        self.status = status
        status_dic = {}
        try:
            with open(self.file_name) as status_file:
                status_dic = json.load(status_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            status_dic['logName'] = self.name
            status_dic['logDate'] = {'date': []}
        date_dic = status_dic['logDate']
        date_dic['date'].append(
            [self.date, (self.test_time(self.start_time, self.end_time)), self.status])
        if JSONValidator.validate(status_dic):
            json.dump(status_dic, open(self.file_name, 'w'))
        else:
            return "Invalid JSON"
        
    def test_time(self, start_time, end_time):
         return (datetime.strptime(self.end_time, '%d%H%M%S%f') - datetime.strptime(self.start_time,'%d%H%M%S%f')).total_seconds()
     
test1 = Logger('T1')
test2 = Logger('T2')

for i in range(100):
    test1.start()
    test2.start()
    test1.end(status.FAIL)
    test2.end(status.FAIL)