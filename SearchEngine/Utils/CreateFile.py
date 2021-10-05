class CreateFile:
    def __init__(self, FileType, Info, FileName):
        self.FileType = FileType
        self.Info = Info
        self.FileName = FileName

    def JSON(self):
        with open(self.FileName, 'w+') as f:
            json.dump(self.Info, f, indent=2)

    def CSV(self):
        pass

    def TXT(self):
        pass