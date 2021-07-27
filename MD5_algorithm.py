import hashlib

def MD5(str2hash):
    result = hashlib.md5(str2hash.encode())

    return f"The hexadecimal equivalent of hash is : {result.hexdigest().upper()}"
