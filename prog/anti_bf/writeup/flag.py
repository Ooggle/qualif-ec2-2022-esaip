import pytesseract
import cv2
import urllib.request
import base64
import urllib.parse
import requests

# get image

page = urllib.request.urlopen('http://challenge01.root-me.org/programmation/ch8/')
pagecontent = str(page.read())

cookies = page.info().get_all('Set-Cookie')
php_session_id = cookies[0][:cookies[0].find(";")]

print("php session id : " + php_session_id)

# print(pagecontent)

pagecontentindex = pagecontent.find('data:image/png;base64,')
pagecontentindexend = pagecontent.find('" /><br><br><form action="" method="POST">')

# base64 string
# print(pagecontent[pagecontentindex + 22:pagecontentindexend])

b64chaine = base64.b64decode(pagecontent[pagecontentindex + 22:pagecontentindexend])

f = open("captcha.png", "wb")
f.write(b64chaine)
f.close()

# get image text
img = cv2.imread('captcha.png')
code = (pytesseract.image_to_string(img))[:12]
code = code.upper()
print("code : \"" + code + "\"")


# send response

url = "http://challenge01.root-me.org/programmation/ch8/"

payload={'username': 'admin', 'password': code,'captcha': code}

print("payload : ")
print(payload)
print()

headers = {
  'Cookie': php_session_id
}

print("headers : ")
print(headers)
print("")

response = requests.request("POST", url, headers=headers, data=payload)

pagecontentindex = response.text.find('data:image/png;base64,')

print(response.text[:pagecontentindex])

# print(response.text)

