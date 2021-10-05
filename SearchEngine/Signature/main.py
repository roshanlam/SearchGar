from lib import read_signing_key_file, create_account_and_save_signing_key_file, create_account, verify_signature
from config import Files
from utils import create_signed_message, write_json, read_json
from nacl.signing import VerifyKey
from db import DB

class Main:
    def __init__(self, message, data, signing_keyFile, signed_messageFile):
        self.message = message
        self.signing_keyFile = signing_keyFile
        self.data = data
        self.signed_messageFile = signed_messageFile
        files = Files(self.signing_keyFile, self.signed_messageFile)
        self.signing_keyFile = files.getSigningKeyFile()
        self.signed_messageFile = files.getSignedMessageFile()
        create_account_and_save_signing_key_file(self.signing_keyFile)
        self.SIGNING_KEY = read_signing_key_file(self.signing_keyFile)

        MESSAGE = self.message
        account_number = self.SIGNING_KEY.verify_key
        signed_message = create_signed_message(
            account_number = account_number,
            message = MESSAGE,
            signing_key = self.SIGNING_KEY,
            data = self.data,
        )
        write_json(file = self.signed_messageFile, data = signed_message)
        self.verifySignature()
        db = DB()
        db.saveSingleInfo(signed_message, 'digitalsignature')


    def verifySignature(self):
        SIGNED_MESSAGE = read_json(self.signed_messageFile)
        try:
            verify_signature(
                message = SIGNED_MESSAGE['message'].encode('utf-8'),
                signature = SIGNED_MESSAGE['signature'],
                verify_key = SIGNED_MESSAGE['account_number'],
                data = SIGNED_MESSAGE['data']
            )
            print('\nSignature is Valid!')
        except Exception as e:
            print('\nSignature is Invalid', e)
