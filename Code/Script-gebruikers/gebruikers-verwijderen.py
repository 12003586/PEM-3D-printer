import requests
import json
import csv

with open("Studenten.csv", 'r') as file:
    csvreader = csv.reader(file)
    studentenmails = next(csvreader)
#print(studentenmails)
    
headers_octoprint={
    'content-type': 'application/json',
    'Host': 'octopi.local',
    'X-Api-Key': '285BD0333BC146CF98AFB9A58CB888D0',
}

for i in range(len(studentenmails)):
    print(i)
    print(studentenmails[i])
    studentNaam = studentenmails[i].split("@")[0]
    studentNaam = studentNaam.replace(".", "-" )
    
    url='http://octopi.local/api/access/users/' + studentNaam
    response =  requests.delete(url,headers=headers_octoprint)
    temp=response.text
    print(response)