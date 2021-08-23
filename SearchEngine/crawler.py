import threading

from domain import *
from general import *
from spider import Spider
from queue import Queue

class Crawler:
    def __init__(self):
        self.project_name = ""
        self.homepage = ""
        self.domain_name = get_domain_name(homepage)
        self.queue_file = project_name + 'queue.txt'
        self.crawled_file = project_name + 'crawled.txt'
        self.num_of_threads = 8
        self.queue = Queue()
        Spider(project_name, home_page, domain_name)

    def create_workers(self):
        for _ in range(self.num_of_threads):
            t = threading.Thread(target = work)
            t.daemon = True
            t.start()

    def work(self):
        while True:
            url = self.queue.get()
            Spider.crawl_page(threading.current_thread().name, url)
            self.queue.task_done()

    def create_job(self):
        for link in file_to_set(self.queue_file):
            self.queue.put(link)
        self.queue.join()
        crawl()

    def crawl(self):
        pass