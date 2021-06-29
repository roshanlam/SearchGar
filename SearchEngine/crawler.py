from locale import getdefaultlocale
import logging
import time
from bs4 import BeautifulSoup
import re
import traceback
from collections import deque
from urllib.parse import urljoin, urlparse

log = logging.getLogger('Main.crawler')

# DO NOT MODIFY/EDIT THIS FILE AS OF RIGHT NOW
# IT IS BEING WORKED ON

class Crawler(object):
    def __init__(self, args):
        self.depth = args.depth
        self.currentDepth = 1
        self.keyword = args.keyword.decode(getdefaultlocale())
        self.database = Database(args.dbFile)
        self.threadPool = ThreadPool(args.dbFile)
        self.visitedHrefs = set()
        self.unvisitedHerfs = deque()
        self.unvisitedHerfs.append(args.url)
        self.isCrawling = False

    def start(self):
        print("Started Crawling")
        if not self._isDatabaseAvaliable():
            print('Error: Unable to Open Database File')
        else:
            self.isCrawling = True
            self.threadPool.startThreads()
            while self.currentDepth < self.depth + 1:
                self._assignCurrentDepthTasks()
                while self.threadPool.getTaskLeft():
                    time.sleep(8)
                print("Depth %d Finished. Totally visited %d links. \n" % (self.currentDepth, len(self.visitedHrefs)))
                log.info('Depth %d Finish. Total visited Links: %d\n' % (
                    self.currentDepth, len(self.visitedHrefs)))
                self.currentDepth += 1
            self.stop()

    def stop(self):
        self.isCrawling = False
        self.threadPool.stopThreads()
        self.database.close()

