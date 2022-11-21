import requests
import json

headers_octoprint={
    'content-type': 'application/json',
    'Host': '172.16.104.231',
    'X-Api-Key': '5F11840C599B4F5DABFC06C403238356',
}

data = {}
data['command'] = 'reboot'
payload = json.dumps(data)
url='http://172.16.104.231:80/api/system/commands/core/reboot'
response =  requests.post(url,data=payload,headers=headers_octoprint)
temp=response.text

print(response)