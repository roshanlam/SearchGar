from nacl.encoding import HexEncoder
from nacl.signing import SigningKey, VerifyKey
from os import path

def encode_verify_key(*, verify_key):
    """Return the hexadecimal representation of the binary account number data"""
    if not isinstance(verify_key, VerifyKey):
        raise RuntimeError('verify_key must be of type nacl.signing.VerifyKey')
    return verify_key.encode(encoder = HexEncoder).decode('utf-8')

def get_verify_key(*, signing_key):
    """Return the verify key from the signing key"""
    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')
    return signing_key.verify_key

def generate_signature(*, message, signing_key):
    """Sign message using signing key and return signature"""
    return signing_key.sign(message).signature.hex()

def verify_signature(*, message, data, signature, verify_key):
    """Verify block signature"""
    verify_key = VerifyKey(verify_key.encode('utf-8'), encoder = HexEncoder)
    signature = bytes.fromhex(signature)
    verify_key.verify(message, data, signature)

def create_account():
    """
    Create a new account
    Return signing_key, account_number
    """
    signing_key = SigningKey.generate()
    account_number = signing_key.verify_key
    return signing_key, account_number

def create_account_and_save_signing_key_file(file):
    """
    Create a new account and save signing key to file
    Return signing_key, account_number
    """
    signing_key, account_number = create_account()
    write_signing_key_file(signing_key, file)
    return signing_key, account_number


def read_signing_key_file(file):
    """Read signing key from file"""
    try:
        with open(file, 'rb') as f:
            return SigningKey(f.read(), encoder=HexEncoder)
    except FileNotFoundError:
        create_account_and_save_signing_key_file(file)

def write_signing_key_file(signing_key, file):
    """Save signing key to file"""
    if not isinstance(signing_key, SigningKey):
        raise RuntimeError('signing_key must be of type nacl.signing.SigningKey')

    if path.exists(file):
        raise RuntimeError(f'{file} already exists')

    with open(file, 'wb') as f:
        f.write(signing_key.encode(encoder=HexEncoder))