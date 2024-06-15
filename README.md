<h1 align="center">✨ 𝔼𝕡𝕚𝕔𝕘𝕒𝕞𝕖𝕤 𝕏𝕒𝕝 ✨</h1>

<p align="center">
  <img src="https://img.shields.io/github/license/H4cK3dR4Du/Epicgames-Xal.svg?style=for-the-badge&labelColor=black&color=c1121f&logo=IOTA"/>
  <img src="https://img.shields.io/github/stars/H4cK3dR4Du/Epicgames-Xal.svg?style=for-the-badge&labelColor=black&color=c1121f&logo=IOTA"/>
  <img src="https://img.shields.io/github/languages/top/H4cK3dR4Du/Epicgames-Xal.svg?style=for-the-badge&labelColor=black&color=c1121f&logo=javascript"/>
</p>

<h2 align="center"> 📝 Description 📝 </h2>

<p align="center">
  This repository is meant to demonstrate how the 'xal' value from <a href="https://epicgames.com/">Epic Games</a> works. Here you will find a lot of information about its functionality and usage. You can also learn how to encrypt/decrypt the value, etc.
</p>

<p align="center">
  <b><big>❤️ Made By H4cK3dR4Du ❤️</big></b>
</p>

<h2 align="center"> 🤷‍♂️ Issues / Doubts 🤷‍♂️</h2>

- **If you have any questions do not hesitate to enter my discord: https://discord.gg/raducord**
- **Or if you have any error do not forget to report it in: [issues](https://github.com/H4cK3dR4Du/Epicgames-Xal/issues/new)**

<h2 align="center"> 🚀 Xal Reverse 🚀 </h2>

### - Requirements And Files:

- **Download Node [here](https://nodejs.org/en/download/package-manager)**
- **Download Python [here](https://www.python.org/downloads/)**

### - XAL Reverse Documentation:

#### - Get XAL Javascript file:

*Okay, first we'll go to the epicgames.com website and open Dev Tools > Sources.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/77305822-77ea-469d-a652-bc995255ff49)

*Here we find an interesting file called 'talon_sdk.js'. If we observe, it's obfuscated. Let's deobfuscate it a bit using a website I really like called https://obf-io.deobfuscate.io/. We'll paste the code there, which will give us a more readable version. Now let's copy that code into a .js file; you can find it in this repository as 'talon_deobfuscated.js'.*

*Now let's start searching for values in the talon.js file. I've created one at files/modified_talon.js where there are modifications that you can review in case you have doubts about how this works.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/4085ce9b-f659-43f9-9018-7e5719c3a1c8)

*The function '_0x37726c' is responsible for constructing the fingerprint before it is encrypted by the '_0x420d7c' function, so let's analyze the code a bit and see how we can view the 'xal' value before it is encrypted.*

*In the 'index.html' file, we will add code to execute the 'files/modified_talon.js' file, so that we can start viewing values using console.log();*

```bash
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Xal Reverse</title>
    <script src="xal.js"></script>
</head>
<body>
    
</body>
</html>
```

*Now let's create a new function in the 'talon.js' file to execute the '_0x37726c' function, which generates the 'xal' fingerprint. We will log the result using console.log('Fingerprint -> ', JSON.stringify(result, null, 2));, so that we can see the 'xal' string before it is encrypted by the '_0x420d7c' function.*

```bash
async function getFingerprint() {
        try {
            const result = await _0x37726c();
            console.log('Fingerprint? -> ', JSON.stringify(result, null, 2));
        } catch (error) {
            console.error("Ok idc", error);
        }
    }

getFingerprint();
```

*Obviously, we will use async and await because we are dealing with a Promise and multiple functions being called concurrently to complete a task.*

*Now, if we open index.html and go to the console, refresh the page, we should see the 'xal' string before it gets encrypted.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/3e61959a-8410-416d-9cab-510d1710db0b)

*Indeed, that's the entire 'xal' value before encryption. It seems to be a fingerprint containing a lot of browser, screen, and hash information. It totals around 400 lines in length. If you'd like to see an example of a fingerprint, you can find it in examples/fingerprint.json.*

*Alright, now let's go directly to the function where they encrypt that fingerprint, which in this case is the function '_0x420d7c'. To ensure that this is indeed the function, you can add a simple console.log(); and print the variable that is passed to the function, like this:*

```bash
function _0x420d7c(_0x4a761c) {
        console.log(JSON.stringify(_0x4a761c, null, 2)); // Add this and Dev Tools > Console to check if it's the fingerprint (it is)
        var _0x2ce575;
        var _0x40db03 = unescape(encodeURIComponent(JSON.stringify(_0x4a761c)));
        var _0x16633c = [];
        var _0x446316 = 0;
        var _0x2e8cf0 = '';
```

*In the same function, we can see a somewhat strange string that appears to be the encryption key they use to encrypt the fingerprint.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/689d11ca-faa7-4100-bdbb-b9696e37fd1a)

*What we need to do is find where the function '_0x420d7c' is called, to know which function we should execute to get the encrypted 'xal' value. In this case, if we search for it in Visual Studio's search, it references the function '_0xcea415', so let's now create a JavaScript code in the .js file similar to the previous one to call the encryption function and see the encrypted 'xal' along with the fingerprint before encryption, thus ensuring we are on the right track.*

```bash
async function getXal() {
      try {
          const result = await _0xcea415();
          console.log('Xal Encrypted -> ', JSON.stringify(result, null, 2));
      } catch (error) {
          console.error("Ok idc", error);
      }
```

*Now if we open index.html, we will see the values of the 2 functions we have executed: first the fingerprint before encryption, and then the encrypted 'xal'.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/6ac6492a-6ddc-47c0-8297-f2c47a48115e)

<h2 align="center"> 🍧 Test Yourself 🍧</h2>

### - Modify Values Fingerprint:

*You can modify the values of the fingerprint to unflag it, and then use encryption.py to encrypt it correctly so that it passes validation in Epic Games. Here's an example code:*

```bash
import json,

fp = json.load(open("examples/fingerprint.json", "r"))
fp["navigator"]["user_agent"] = "User Agent You Want"

print(fp)
```

### - Decrypt XAL:

*I have created a file called decrypt.py for you to decrypt your 'xal' value. Simply replace 'Xal here' with your actual xal, and it will be saved in 'results/decrypted_xal.txt'.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/d50b8183-0108-4434-a697-96ce80c4f57a)

### - Encrypt XAL:

*The same as before, another file but named encrypt.py, you just have to replace 'fingerprint' with the modified fingerprint you have created. This way you'll encrypt your fingerprint and Epic Games will accept it as valid. I can give you an example:*

```py
# Using encrypt.py:

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

fp = json.load(open("examples/fingerprint.json", "r"))
fp["navigator"]["user_agent"] = "User Agent You Want"
fp["document"]["title"] = "Radu nooby"

xal_encrypted = encode_data(fp)
print(xal_encrypted)
```

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/d5796ba9-32c5-4398-8af2-e469c3002b80)
