import json
import base64
from datetime import datetime
import random
import string
import time
import hashlib

def encode_data(a):
    xxx = "FZMÛSê/·V«xÞhí¢³4<`ô2ª,µ¦Yû"
    b = 0
    c = json.dumps(a).encode('utf-8')
    d = list(range(256))
    e = 0
    f = ""

    for h in range(256):
        e = (e + d[h] + ord(xxx[h % len(xxx)])) % 256
        b = d[h]
        d[h] = d[e]
        d[e] = b

    i = 0
    e = 0

    for j in range(len(c)):
        i = (i + 1) % 256
        e = (e + d[i]) % 256
        b = d[i]
        d[i] = d[e]
        d[e] = b
        f += chr(c[j] ^ d[(d[i] + d[e]) % 256])

    encrypted = base64.b64encode(f.encode('latin-1')).decode('latin-1')

    with open('results/encrypted_xal.txt', 'w') as file:
        file.write(encrypted + "\n")

    return encrypted

xal_encrypted = encode_data("fingerprint")
print(xal_encrypted)