class checkWebsite(status = None):
    process = 0 # stale
    
    def __init__(self):
        #self.status = status
        #self.process = process
        pass
    
    def check(url):
        if(len(url) > 1):
            print("Checking URl....")
        else:
            print("The length of url is invalid")
        
