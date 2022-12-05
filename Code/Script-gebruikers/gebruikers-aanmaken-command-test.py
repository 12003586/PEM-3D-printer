import requests
import json

headers_octoprint={
    'content-type': 'application/json',
    'Host': 'octopi.local',
    'X-Api-Key': '285BD0333BC146CF98AFB9A58CB888D0',
}

data = {}
data['command'] = 'reboot'
payload = json.dumps(data)
url='http://octopi.local/api/system/commands/core/reboot'
response =  requests.post(url,data=payload,headers=headers_octoprint)
temp=response.text

print(response)