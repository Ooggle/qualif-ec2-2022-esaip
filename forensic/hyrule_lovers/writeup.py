from base64 import b64decode
from re import findall

with open(file="dist/apache.log", mode="r") as file:
    logs = file.read().split("\n")

for i in range(len(logs)):
    search = findall('search=(.*?)"', logs[i])[0]
    search = b64decode(search).decode()
    if "location" in search:
        print(search)
        print(logs[i+1])

print(b64decode(b64decode("Wm14aFp6MVNNa3hwYkd4bGUwaDVVblZNTTE5WVUxTmZUREIyTTFKOQ==").decode()))
