import requests
import json

headers_octoprint={
    'content-type': 'application/json',
    'Host': 'octopi.local',
    'X-Api-Key': '285BD0333BC146CF98AFB9A58CB888D0'
}

data = {"name":"Python123","password":"123456","groups":["studenten"],"permissions":[],"active":'true',"admin":'false'}

payload = json.dumps(data)
url='http://172.16.104.231:80/api/access/users'
response =  requests.post(url,data=payload,headers=headers_octoprint)
temp=response.text

print(response)
