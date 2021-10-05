import os

class Files:
    def __init__(self, signingKeyFile, SignedMessageFile):
        self.signingKeyFile = signingKeyFile
        self.SignedMessageFile = SignedMessageFile
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.SIGNING_KEY_FILE = os.path.join(BASE_DIR, self.signingKeyFile)
        self.SIGNED_MESSAGE_FILE = os.path.join(BASE_DIR, self.SignedMessageFile)

    def getSigningKeyFile(self):
        return self.SIGNING_KEY_FILE

    def getSignedMessageFile(self):
        return self.SIGNED_MESSAGE_FILE
