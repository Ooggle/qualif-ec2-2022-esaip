from multiprocessing import Process
from random import randint
from time import time
import socket

# Init
banner = b"""
,--.   ,--.              ,---.,--.               ,--.             ,--.                    
|   `.'   |,--. ,--.    /  .-'`--',--.--. ,---.,-'  '-.     ,---. |  ,---.  ,---.  ,---.  
|  |'.'|  | \  '  /     |  `-,,--.|  .--'(  .-''-.  .-'    (  .-' |  .-.  || .-. || .-. | 
|  |   |  |  \   '      |  .-'|  ||  |   .-'  `) |  |      .-'  `)|  | |  |' '-' '| '-' ' 
`--'   `--'.-'  /       `--'  `--'`--'   `----'  `--'      `----' `--' `--' `---' |  |-'  
           `---'                                                                  `--'    
           
           \n"""
shop = ["shields", "swords", "potions", "bows", "arrows", "hammers", "boomerangs", "bottles"]
clients = [("Link", "He"), ("Zelda", "She"), ("Ganon", "He"), ("Impa", "She"), ("Navi", "She"), ("Riju", "She"), ("Midna", "She")]


# Close socket if 2s timeout is being reach
def too_late(s):
    s.send(b'Too Late !\n')
    exit(0)


# Wrong answer
def wrong_answer(s):
    s.send(b'Wrong Answer !\n')
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
        # Checking for 2s timeout
        check = time()
        if int(check - start) >= 2:
            too_late(s)
    return body


# Challenge
def challenge(s):
    s.send(banner)
    s.send(b"Welcome adventurer, I heard that you're looking for precious treasures.\nI can offer you one of thoses, but first need to handle 100 of my clients in a row.\nI will come back when you are finished.\nGood luck!\n\n")

    for i in range(1, 101):
        s.send(f"--------------------\nClient n°{i}:\n".encode())
        num1 = randint(0,999999)
        num2 = randint(0,999999)
        item1 = shop[randint(0,len(shop)-1)]
        item2 = shop[randint(0,len(shop)-1)]
        client = clients[randint(0,len(clients)-1)]

        if i <= 25:
            solution = str(num1 + num2)
            s.send(f"{client[0]} enters the shop...\n".encode())
            s.send(f"{client[1]} want to buy a {item1[:-1]} ({num1} rupees) and a {item2[:-1]} ({num2} rupees). How much will {client[1]} paid for it?".encode() + b"\n")
        elif i > 25 and i <= 50:
            solution = str(num1 - num2)
            s.send(f"{client[0]} enters the shop...\n".encode())
            s.send(f"{client[1]} want to buy a {item1[:-1]} ({num1} rupees) and sell a {item2[:-1]} ({num2} rupees). How much will {client[1]} paid for it?".encode() + b"\n")
        elif i > 50 and i <= 75:
            solution = str(num1 * num2)
            s.send(f"{client[0]} enters the shop...\n".encode())
            s.send(f"{client[1]} want to buy {num1} {item1} ({num2} rupees). How much will {client[1]} paid for it?".encode() + b"\n")
        elif i > 75:
            solution = str(num1*num2 - num2*num1)
            s.send(f"{client[0]} enters the shop...\n".encode())
            s.send(f"{client[1]} want to buy {num1} {item1} ({num2} rupees) and sell {num2} {item2} ({num1} rupees). How much will {client[1]} paid for it?".encode() + b"\n")

        response = read_line(s).decode()
        if response == solution:
            s.send(f"{client[0]} paid and leave the shop...\n".encode())
        else:
            wrong_answer(s)
    
    # Send the flag
    s.send(b"Well done master! You made it, this is a treasure ...: R2Lille{}\n")
    exit(0)


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
