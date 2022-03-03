from flask import Flask, request
from datetime import datetime
from base64 import b64encode
from jinja2 import Template
from random import randint

"""
I manualy added admin log lines:
143.175.179.171 - - [**] "GET https://hyruleforever.ec2qualifications.esaip-cyber.com?search=PGltZyBzcmM9eCBvbmVycm9yPSJkb2N1bWVudC5sb2NhdGlvbi5wYXRobmFtZSA9IGAvJHthdG9iKGRvY3VtZW50LmNvb2tpZSl9YCI+" "ooggle.re :)"
143.175.179.171 - - [**] "GET https://hyruleforever.ec2qualifications.esaip-cyber.com?search=Wm14aFp6MVNNa3hwYkd4bGUwaDVVblZNTTE5WVUxTmZUREIyTTFKOQ==" "ooggle.re :)"
"""


# Init
user_agents = ["Mozilla/1.22 (compatible; MSIE 2.0d; Windows NT)", "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:0.9.2) Gecko/20010726 Netscape6/6.1", "Wget/1.8.2", "Opera/9.27 (Windows NT 5.1; U; en)", "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.5) Gecko/2008120121 Firefox/3.0.5", "AppleWebKit/525.19 (KHTML&#44; like Gecko) Chrome/0.2.153.1 Safari/525.19", "SearchSight/2.0 (http://SearchSight.com/)", "mizu.re :)", "ooggle.re :)"]
random_ip = [(f"{randint(70,220)}.{randint(70,220)}.{randint(70,220)}.{randint(70,220)}", user_agents[randint(0, len(user_agents)-1)]) for i in range(100)]
attacker = ("152.168.131.217", "mizu.re :)")
with open(file="xss-payload-list.txt", mode="r") as file:
    xss_wordlist = file.read().split("\n")
with open(file="zelda-wordlist.txt", mode="r") as file:
    zelda_wordlist = file.read().split("\n")

# Create empty log file
with open(file="apache.log", mode="w") as file:
    file.write("")


# Create the APP
app = Flask(__name__)


# Error handler
@app.errorhandler(404)
def page_not_found(error):
    # Avoid favicon query inside logs
    if "favicon" in request.url:
        return ""

    # Init / Random for attacker
    if randint(0, 10) == 7:
        url = f"https://hyruleforever.ec2qualifications.esaip-cyber.com?search={b64encode(xss_wordlist[randint(0, len(xss_wordlist)-1)].encode()).decode()}"
        user = attacker
    else:
        url = f"https://hyruleforever.ec2qualifications.esaip-cyber.com?search={b64encode(zelda_wordlist[randint(0, len(zelda_wordlist)-1)].encode()).decode()}"
        user = random_ip[randint(0, len(random_ip)-1)]
    
    date = datetime.now()
    date = date.strftime("%d/%b/%Y:%H:%M:%S +0000")	

    # Generate logs
    log = '{{ip}} - - [{{date}}] "GET {{url}}" "{{user_agent}}"'
    log = Template(log).render(ip=user[0], date=date, url=url, user_agent=user[1])

    # Open to append
    with open(file="apache.log", mode="a") as file:
        file.write(log + "\n")

    # Return logs
    return log


if __name__ == "__main__":
    # Starting app
    app.run("0.0.0.0", port=5000)
