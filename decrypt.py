import base64
import json

def decrypt(xal):
    key = "FZMÛSê/·V«xÞhí¢³4<`ô2ª,µ¦Yû"
    d = list(range(256))
    e = 0
    f = []

    for h in range(256):
        e = (e + d[h] + ord(key[h % len(key)])) % 256
        d[h], d[e] = d[e], d[h]

    i = 0
    e = 0
    c = base64.b64decode(xal)

    for j in range(len(c)):
        i = (i + 1) % 256
        e = (e + d[i]) % 256
        d[i], d[e] = d[e], d[i]
        f.append(chr(c[j] ^ d[(d[i] + d[e]) % 256]))

    yes = ''.join(f)
    yes = bytearray(yes, 'utf-8').decode('unicode_escape')

    x = json.loads(yes)
    x_string = json.dumps(x)

    with open('results/decrypted_xal.txt', 'w') as file:
        file.write(x_string + "\n")

    return x

xal = decrypt('Xal here')
print(json.dumps(xal, indent=4))