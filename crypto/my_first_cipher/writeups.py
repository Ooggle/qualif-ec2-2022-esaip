with open(file="flag.enc", mode="r") as file:
    cipher_text = file.read()

for x in range(12):
    clear_text = ""
    for i in range(len(cipher_text)):
        clear_text += chr(ord(cipher_text[i]) - x)
    print(clear_text)
