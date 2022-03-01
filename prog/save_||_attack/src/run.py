from multiprocessing import Process
from base64 import b64encode
from random import randint
from json import loads
from io import BytesIO
from time import time
from PIL import Image
import socket

# Banner
banner = b"""
.____    .__        __       _____.__       .__     __                
|    |   |__| ____ |  | __ _/ ____\__| ____ |  |___/  |_  ___________ 
|    |   |  |/    \|  |/ / \   __\|  |/ ___\|  |  \   __\/ __ \_  __ \\
|    |___|  |   |  \    <   |  |  |  / /_/  >   Y  \  | \  ___/|  | \/
|_______ \__|___|  /__|_ \  |__|  |__\___  /|___|  /__|  \___  >__|   
        \/       \/     \/          /_____/      \/          \/       

"""


# Get random image
def getRImage():
    # Select image
    solution = ""
    if randint(0, 1) == 0:
        file = f"images/ally/{randint(1, 6)}.jpg"
        solution = "save"
    else:
        file = f"images/monster/{randint(1, 10)}.jpg"
        solution = "attack"
    # Open image
    img = Image.open(file)
    pixels = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixels[x,y] = (pixels[x,y][0]+randint(-1,1), pixels[x,y][1]+randint(-1,1), pixels[x,y][2]+randint(-1,1))
    # Converte image to base64
    buf = BytesIO()
    img.save(buf, format='JPEG')
    # return image
    return solution, b64encode(buf.getvalue())


# Wrong user answer
def wrong_answer(s):
    s.send(b'Wrong Answer !\n')
    exit(0)

# Close socket if 5s timeout is being reach
def too_late(s):
    s.send(b'Too Late !\n')
    exit(0)


# Get user input
def read_line(s):
    start = time()
    body = b""
    while True:
        ch = s.recv(1)
        if ch == b"\n":
            break
        body = body + ch
        # Checking for 5s timeout
        check = time()
        if int(check - start) >= 5:
            too_late(s)
    return body


# Challenge
def challenge(s):
    # Init
    s.send(banner)
    s.send(b"Hey Link! A lot of monsters have invade Hyrule, please help me saving everyone!\n\n")
    s.send(b"How to play:\n")
    s.send(b"You will recieve an image, after identifying if it's an ally or a monster, send us the following:\n")
    s.send(b'{"solution": "save"} or {"solution": "attack"}\n\n')
    s.send(b'Send: "start" to start a party\n\n')

    msg = read_line(s)
    if msg == b"start":
        # Game start
        for i in range(1, 51):
            solution, img = getRImage()
            s.send(img + b"\n\n")
            s.send(b"Link, what do we do?!\n")
            try:
                user_reponse = loads(read_line(s).decode())
                if not user_reponse["solution"] == solution:
                    wrong_answer(s)
            except:
                wrong_answer(s)
    else:
        exit(0)

    s.send(b"Well played Link! We made it! As a reward this is for you: R2Lille{4lly_0R_3n3my_Th4T_1s_Th3_1A_Qu3St10N}\n")


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
