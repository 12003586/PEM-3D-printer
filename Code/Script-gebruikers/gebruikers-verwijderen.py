import requests
import csv
import time


with open("Studenten.csv", 'r') as file:
    csvreader = csv.reader(file)
    studentenmails = next(csvreader)
#print(studentenmails)
    
headers_octoprint={
    'content-type': 'application/json',
    'Host': 'http://octopi.pxl-ea-ict.be:24081',
    'X-Api-Key': '285BD0333BC146CF98AFB9A58CB888D0',
}

for i in range(len(studentenmails)):
    print(i)
    print(studentenmails[i])
    studentNaam = studentenmails[i].split("@")[0]
    studentNaam = studentNaam.replace(".", "-" )
    
    url='http://octopi.pxl-ea-ict.be:24081/api/access/users/' + studentNaam
    
    print(url)
    
    response =  requests.delete(url,headers=headers_octoprint)
    temp=response.text
    print(response)
    
    #Enkel nodig wanneer octopi.local gebruikt wordt ipv een ip-adres door dns problemen
    time.sleep(5) 

