from pwn import remote
from re import findall

s = remote("hyruleshop.ec2qualifications.esaip-cyber.com", 55555)

# Remove useless output
s.recvuntil(b"enters the shop...\n")

for i in range(1, 101):
    # Get articles line
    prices = s.recvuntil(b"paid for it?\n").decode()
    prices = findall("([0-9]+?) ", prices)

    # Compute
    if i <= 25:
        solution = int(prices[0]) + int(prices[1])
    elif i > 25 and i <= 50:
        solution = int(prices[0]) - int(prices[1])
    elif i > 50 and i <= 75:
        solution = int(prices[0]) * int(prices[1])
    elif i > 75:
        solution = int(prices[0]) * int(prices[1]) - int(prices[2]) * int(prices[3])

    # Send response
    s.sendline(f"{solution}".encode())

# Retrieve the flag
flag = s.recvall().decode().split("\n")[1]
print(flag)
