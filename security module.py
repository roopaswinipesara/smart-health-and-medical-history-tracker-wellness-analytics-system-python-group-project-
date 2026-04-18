import hashlib

users = {}

def encrypt(password):
    return hashlib.sha256(password.encode()).hexdigest()