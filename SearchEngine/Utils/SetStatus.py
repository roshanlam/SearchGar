class SetStatus:
    # 1 - Running
    # 2 - Stale (Not Running)
    # 3 - Failed
    status = None
    def __init__(self):
        self.status = status

    def Running(self):
        self.status = 1

    def Stale(self):
        self.status = 2

    def Failed(self):
        self.status = 3

