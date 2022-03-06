from multiprocessing import Process
from Crypto.Cipher import AES
from base64 import b64decode
from re import findall
from json import loads
from time import time
import socket

"""
Cipher init

admin key clear text: 0000000000000000{"name":"Link","unlock":true}000
admin key cipher text: *sensored*

For debugging purpose:
guest key clear text: 0000000000000000{"name":"Test","unlock":true}000
guest key cipher text: ZyYw4tCA7STmjqKuRnW3/VrPXhpo/NhAiHLgpxs6HVR8WpAn9j8lhb8pH90WKhVE==
"""
secret_key = b"2a918656b23f4b7e"
secret_iv = b"4b015198b15258cd"
cipher = AES.new(secret_key, AES.MODE_CBC, secret_iv)

# Ascii art init
close_chest = """ 
            ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░
          ▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
          ▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░██
        ▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
      ██▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░░░██
      ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░░░▓▓▒▒▒▒▒▒▒▒▒▒░░░░██
      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
      ██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓░░▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓░░▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
        ██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
          ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓░░██
          ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██
          ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░██
          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
          ░░  ░░░░░░░░░░░░░░    ░░    ░░\n\n"""

open_chest = """
                    ▓▓▓▓                    
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
        ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
        ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
        ▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▓▓░░░░░░▓▓▓▓▓▓▓▓
        ▓▓▓▓▓▓▓▓▓▓░░░░░░░░▓▓▒▒░░░░░░▓▓▓▓▓▓▓▓
        ▓▓░░▓▓▓▓░░░░░░░░░░░░░░░░░░░░▓▓▓▓░░▓▓
        ▓▓░░▓▓░░░░▒▒░░░░░░░░▒▒▒▒░░░░░░▓▓░░▓▓
        ▓▓░░▓▓░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
      ▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▒▒
      ▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒
      ▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒
      ▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒
      ▒▒▓▓░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓░░▓▓▒▒
      ▒▒▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓▒▒
      ▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒
      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒
      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░\n\n"""


# Get user input
def read_line(s):
    start = time()
    body = b""
    while True:
        ch = s.recv(1)
        if ch == b"\n":
            break
        body = body + ch
    return body


# Flag
def flag(s, key):
    if key["name"] == "Link" and key["unlock"] == 1:
        s.send(b"\n\033[37;1mWellcome back \033[32;1mLink\033[37;1m, there is your treasure:\033[0m")
        s.send(open_chest.encode())
        s.send(b"\033[37;1mFlag: \033[32;1mR2Lille{d0_n07_Fl1P_Th4t_FuCK1nG_cH3ST!!}\033[0m")
    elif key["name"] == "Test" and key["unlock"] == 1:
        s.send(b"\n\033[32;1mTesting key accepted! Closing...\033[0m")
    else:
        s.send(b"\n\033[31;1m=== WRONG KEY ===\033[0m")


# Challenge
def challenge(s):
    s.send(b"\n")
    s.send(close_chest.encode())
    s.send(b"\033[37;1mYou didn't provide any key while starting the program. Send me your key to unlock the chest please:\033[0m\n")
    cipher_key = read_line(s).decode()
    try:
        key = cipher.decrypt(b64decode(cipher_key))
    except:
        s.send(b"\n\033[31;1m=== KEY ERROR ===\033[0m\n\n")
        return False
    try:
        key = loads(findall(b"{.*?}", key)[0])
    except:
        s.send(b"\n\033[31;1m=== LOADING JSON ERROR ===\033[0m\n\n")
        return False
    flag(s, key)
    s.send(b"\n\n")
    return True


# Main
if __name__ == '__main__':
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 55555))
    s.listen(10)
    while True:
        client, addr = s.accept()
        print(f"Got connect from {addr}")
        p = Process(target=challenge, args=(client,))
        p.daemon = True
        p.start()
        client.close()
