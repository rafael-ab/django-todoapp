import os
from binascii import hexlify

def get_secret_key(filename):
    if check_secret_key(filename):
        with open(filename, 'r') as file:
            secret_key = file.read()
    else:
        secret_key = generate_secret_key()
        with open(filename, 'w') as file:
            file.write(secret_key)
    return secret_key
    
def check_secret_key(filename):
    return os.path.exists(filename)

def generate_secret_key():
    return hexlify(os.urandom(30)).decode()
