from random import random
from requests import get
from time import sleep


# Starting bot
for i in range(1394):
    get("http://localhost:5000/")
    sleep(random())
