import os
import uuid
import hashlib


def generate_salt(length=32):
    return os.urandom(length)


def generate_user_id():
    salt = generate_salt()
    raw_id = str(uuid.uuid4()).encode('utf-8')
    salted_id = salt + raw_id
    hashed_id = hashlib.sha256(salted_id).hexdigest()
    return hashed_id
