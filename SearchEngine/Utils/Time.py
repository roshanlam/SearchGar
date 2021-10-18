from datetime import datetime
import time
from enum import IntEnum
import json
import os


class Status(IntEnum):
    running = 301
    failed = 302
    success = 303
    stale = 304


class Time:
    test_name = None
    test_date = None
    test_status = None
    test_start_time = None
    test_end_time = None
    test_file_name = None

    def __init__(self, name):
        self.test_date = datetime.today().strftime('%Y%m%d%H%M%S')
        self.test_status = Status.stale
        self.test_start_time = datetime.today().strftime('%d%H%M%S%f')
        self.test_name = name
        self.test_file_name = 'status/' + self.test_name + '_status.json'

    def startTest(self):
        if self.test_status is Status.running:
            raise Exception('Test  {} is already running'.format(self.test_name))
        self.test_status = Status.running

    def endTest(self, status):
        if not (self.test_status is Status.running):
            raise Exception('Test {} is not Running'.format(self.test_name))
        if not os.path.exists('status'): os.makedirs('status')
        self.test_end_time = datetime.today().strftime('%d%H%M%S%f')
        self.test_status = status
        test_status_dic = {}
        try:
            with open(self.test_file_name) as test_status_file:
                test_status_dic = json.load(test_status_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError) as e:
            test_status_dic['testName'] = self.test_name
            test_status_dic['testDate'] = {'date': []}
        test_date_dic = test_status_dic['testDate']
        test_date_dic['date'].append(
            [self.test_date, (self.test_time(self.test_start_time, self.test_end_time)), self.test_status])
        json.dump(test_status_dic, open(self.test_file_name, 'w'))

    def resetTestStatus(self):
        pass

    def test_time(self, test_start_time, test_end_time):
        test_duration = (datetime.strptime(test_end_time, '%d%H%M%S%f') - datetime.strptime(test_start_time,'%d%H%M%S%f')).total_seconds()
        return test_duration


test1 = Time('T1')
test2 = Time('T2')

for i in range(100):
    test1.startTest()
    test2.startTest()
    time.sleep(5)
    test1.endTest(Status.failed)
    test2.endTest(Status.failed)