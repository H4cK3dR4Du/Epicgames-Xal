import json

fp = json.load(open("examples/fingerprint.json", "r"))
fp["navigator"]["user_agent"] = "User Agent You Want"

print(fp)