import requests
import json
import smtplib
import string
import random
import time

import csv

with open("Studenten.csv", 'r') as file:
    csvreader = csv.reader(file)
    studentenmails = next(csvreader)
#print(header)
    
#testing zonder csv
#studentenmails = ["Martijn.Guilliams@student.pxl.be", "Bo.Mengels@student.pxl.be", "Gijs.Jackers@student.pxl.be"]
    
length = 10
characterList = ""
characterList += string.ascii_letters
characterList += string.digits
characterList += string.punctuation

# Server instellingen
MailServerAdres = "smtp.office365.com"
MailServerPoort = "587"
MailServerLogin = "Octoprint@outlook.be"
MailServerPass = "na7yDLBdi7Qnw5"
 
# Mail bericht
MailZender = "Octoprint@outlook.be"
MailOnderwerp = "Login OctoPi"

headers_octoprint={
    'content-type': 'application/json',
    'Host': 'octopi.pxl-ea-ict.be:24081',
    'X-Api-Key': '285BD0333BC146CF98AFB9A58CB888D0',
}

for i in range(len(studentenmails)):
    print(i)
    print(studentenmails[i])
    studentNaam = studentenmails[i].split("@")[0]
    studentNaam = studentNaam.replace(".", "-" )
    studentMail = studentenmails[i]
    
    password = []

    for j in range(length):
        # Picking a random character from our
        # character list
        randomchar = random.choice(characterList)

        # appending a random character to password
        password.append(randomchar)

    # printing password as a string
    print("The random password is " + "".join(password))
    studentWachtwoord = "".join(password)

    data = {"name":studentNaam,"password":studentWachtwoord,"groups":["studenten"],"permissions":[],"active":'true',"admin":'false'}
    payload = json.dumps(data)
    url='http://octopi.pxl-ea-ict.be:24081/api/access/users'
    response =  requests.post(url,data=payload,headers=headers_octoprint)
    temp=response.text
    
    # Contact  maken met mailserver
    mailserver = smtplib.SMTP(MailServerAdres, MailServerPoort)
    mailserver.starttls() # TLS versleuteling nodig voor Hotmail/Gmail (werkt ook met Hostnet)
    mailserver.login(MailServerLogin, MailServerPass)
     
    # Bericht samenstellen
    MailBericht = "Gebruikersnaam: " + studentNaam + "\n\nWachtwoord: " + studentWachtwoord
    bericht = 'To:' + studentenmails[i]  + '\n' + 'From: ' + MailZender + '\n' + 'Subject:' + MailOnderwerp + '\n\n' + MailBericht + '\n\n'
    
    print(response)
    
    # Mail verzenden
    try:
      mailserver.sendmail(MailZender, studentenmails[i], bericht)
      print ("OK: email verzonden")
    except SMTPException:
      print ("FOUT: kan email niet verzenden!")
      
    # 
    # Enkel nodig wanneer octopi.local gebruikt wordt ipv een ip-adres door dns problemen
    time.sleep(5) 

