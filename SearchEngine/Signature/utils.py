import json
from lib import encode_verify_key

def create_signed_message(*, account_number, message, signing_key, data):
    block = {
        'account_number': encode_verify_key(verify_key = account_number),
        'message': message,
        'signature': signing_key.sign(message.encode('utf-8')).signature.hex(),
        'data': data
    }
    return block

def read_json(file):
    try:
        with open(file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = None
    return data

def write_json(file, data):
    with open(file, 'w') as file:
        json.dump(data, file, indent = 2)

