class Spider:
    allowed_domains = ['.com', '.org', '.gov', '.edu']
    start_crawl = []
    def __init__(self, start_crawl):
        self.start_crawl = [start_crawl]
        self.handles = {}

    def parse(self, reponse):
        pass
