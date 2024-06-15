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

- **Download Node [here]([https://hex-rays.com/ida-free/](https://nodejs.org/en/download/package-manager))**
- **Download Python [here](https://www.python.org/downloads/)**

### - XAL Reverse Documentation:

#### - Get XAL Javascript file:

*Okay, first we'll go to the epicgames.com website and open Dev Tools > Sources.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/77305822-77ea-469d-a652-bc995255ff49)

*Here we find an interesting file called 'talon_sdk.js'. If we observe, it's obfuscated. Let's deobfuscate it a bit using a website I really like called https://obf-io.deobfuscate.io/. We'll paste the code there, which will give us a more readable version. Now let's copy that code into a .js file; you can find it in this repository as 'talon_deobfuscated.js'.*

*Now let's start searching for values in the talon.js file. I've created one at files/modified_talon.js where there are modifications that you can review in case you have doubts about how this works.*

![image](https://github.com/H4cK3dR4Du/Epicgames-Xal/assets/118562174/4085ce9b-f659-43f9-9018-7e5719c3a1c8)

*The function '_0x37726c' is responsible for constructing the fingerprint before it is encrypted by the '_0xcea415' function, so let's analyze the code a bit and see how we can view the 'xal' value before it is encrypted.*

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

*Now let's create a new function in the 'talon.js' file to execute the '_0x37726c' function, which generates the 'xal' fingerprint. We will log the result using console.log('Fingerprint -> ', JSON.stringify(result, null, 2));, so that we can see the 'xal' string before it is encrypted by the '_0xcea415' function.*

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

