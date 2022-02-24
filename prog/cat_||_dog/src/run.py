from multiprocessing import Process
from base64 import b64encode
from random import randint
from io import BytesIO
from time import time
from PIL import Image
import socket


# Get random image
def getRImage():
    # Select image
    if randint(0, 1) == 0:
        file = f"kaggle_dataset/Cat/{randint(0, 12499)}.jpg"
    else:
        file = f"kaggle_dataset/Dog/{randint(0, 12499)}.jpg"
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
    return b64encode(buf.getvalue())


# Close socket if 7s timeout is being reach
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
        # Checking for 7s timeout
        check = time()
        if int(check - start) >= 7:
            too_late(s)
    return body


# Challenge
def challenge(s):
    s.send(getRImage())


# Main
if __name__ == '__main__':
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", 4444))
    s.listen(10)
    while True:
        client, addr = s.accept()
        print(f"Got connect from {addr}")
        p = Process(target=challenge, args=(client,))
        p.daemon = True
        p.start()
        client.close()
