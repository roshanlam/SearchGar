from datetime import datetime
from enum import IntEnum
import os
import json
import time

class Status(IntEnum):
    running = 301
    failed = 302
    success = 303
    stale = 304

# Logger will used to log information and saved information by default
# TODO: If user tries to search a query and there is an error then the query, and other techical info would be automatically sent through an email
class Logger:
    log_date = None
    log_status = None
    log_start_time = None
    log_end_time = None
    log_file_name  = None
    def __init__(self, name):
        self.log_date = datetime.today().strftime('%Y%m%d%H%M%S')
        self.log_status = Status.stale
        self.log_start_time = datetime.today().strftime('%d%H%M%S%f')
        self.log_name = name
        self.log_file_name = 'log-status/' + self.log_name + '_log-status.json'

    def startLog(self):
        if(self.log_status is Status.running):
            raise Exception('Logging is already running {}'.format(self.log_name))
        self.log_status = Status.running

    def endLog(self, status):
        if not (self.log_status is Status.running):
            raise Exception('Logging is not running {}'.format(self.log_name))
        if not os.path.exists('status'):
            os.makedirs('log-status')
        self.log_end_time = datetime.today().strftime('%d%H%M%S%f')
        self.log_status = status
        log_status_dic = {}
        try:
            with open(self.log_file_name) as log_status_file:
                log_status_dic = json.load(log_status_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            log_status_dic['logName'] = self.log_name
            log_status_dic['logDate'] = {'date': []}
        log_date_dic = log_status_dic['logDate']
        log_date_dic['date'].append([self.log_date,
        (self.log_time(self.log_start_time, self.log_end_time)), self.log_status])
        json.dump(log_status_dic, open(self.log_file_name, 'w'))

    def log_time(self, log_start_time, log_end_time):
        log_duration = (datetime.strptime(log_end_time, '%d%H%M%S%f') -
                        datetime.strptime(log_start_time, '%d%H%M%S%f')).total_seconds()
        return log_duration

log_test1 = Logger('T1')
log_test2 = Logger('T2')

for i in range(10):
    log_test1.startLog()
    log_test2.startLog()
    time.sleep(5)
    log_test1.endLog(Status.failed)
    log_test2.endLog(Status.failed)

# ToDo: Make this logger better (this logger is just a draft, in way) and intregate it with the search engine
