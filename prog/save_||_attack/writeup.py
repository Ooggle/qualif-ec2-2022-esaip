from base64 import b64decode
from json import dumps
from io import BytesIO
from pwn import remote
from PIL import Image

"""
1°) Dump all possible images.
2°) Compute zone of monster corn that will help to detect them
3°) Create the following script and flag chall
"""

# Init
s = remote("saveattack.ec2qualifications.esaip-cyber.com", 55555)
s.recvuntil(b"to start a party\n\n")
s.sendline(b"start")

# Start challenge
for i in range(1, 51):
    print(f"\r\x1b[1mQuestion n°{i}\x1b[0m", end="")
    # Get image
    try:
        x = s.recvline().decode()
        img = b64decode(x)
    except:
        print(x)
        exit()
    img = Image.open(BytesIO(img))
    # Counting white pixel
    pixels = img.load()
    response = dumps({"solution": "save"})

    for x in range(10): # Top right zone
        for y in range(760, 770):
            if pixels[y,x][0] <= 240 or pixels[y,x][1] <= 240 or pixels[y,x][2] <= 240:
                response = dumps({"solution": "attack"})

    for x in range(320, 350): # Middle left zone
        for y in range(5):
            if pixels[y,x][0] <= 240 or pixels[y,x][1] <= 240 or pixels[y,x][2] <= 240:
                response = dumps({"solution": "attack"})
    # Send answer
    s.recvuntil(b"Link, what do we do?!\n")
    s.sendline(response.encode())

print(s.recvall())
