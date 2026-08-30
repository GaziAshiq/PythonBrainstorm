import requests
import sys

baseurl = "http://subeen.com/download/"

info_ft = {'name': 'Ashiq', 'email': 'ashiqgazi@a.com', 'country': 'BD'}

url = baseurl + 'process.php'

res = requests.post(url, info_ft)

if res.ok is False:
    sys.exit('error downloading file' + res.reason)

with open('cpbook.pdf', 'wb', encoding=res.encoding) as f:
    f.write(res.content)

print("book download complete")