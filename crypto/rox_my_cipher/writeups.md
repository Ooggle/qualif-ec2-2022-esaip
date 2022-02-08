# Writeup

<br>

```py
clear_text = ""
with open(file="flag.enc", mode="r") as file:
    cipher_text = file.read()

cut = int(len(cipher_text)/2)
cipher_text = cipher_text[cut:] + cipher_text[:cut]

for i in range(len(cipher_text)):
    clear_text += chr(ord(cipher_text[i]) ^ key[i % len(key)])

print(clear_text)
```
