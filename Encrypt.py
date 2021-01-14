from pybase64 import b64encode,b64decode
password = input().encode("utf-8")
encoded = b64encode(password)
print(encoded)
decoded = b64decode(encoded)
print(decoded)