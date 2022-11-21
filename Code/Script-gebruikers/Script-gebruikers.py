import requests
import json
import smtplib


studentenmails = ["Martijn.Guilliams@student.pxl.be","Gijs.Jackers@student.pxl.be","Bo.Mengels@student.pxl.be"]


for i in studentenmails:
    print(x)
    studentNaam = studentenmails[i].split(':')[0]
    studentMail = studentenmails[i]
    studentWachtwoord = 

    headers_octoprint={
        'content-type': 'application/json',
        'Host': '172.16.104.231',
        'X-Api-Key': '5F11840C599B4F5DABFC06C403238356',
    }

    data = {"name":studentNaam,"password":"123456","groups":["studenten"],"permissions":[],"active":'true',"admin":'false'}

    payload = json.dumps(data)
    url='http://172.16.104.231:80/api/access/users'
    response =  requests.post(url,data=payload,headers=headers_octoprint)
    temp=response.text

    print(response)





    # Server instellingen
    MailServerAdres = "smtp.office365.com"
    MailServerPoort = "587"
    MailServerLogin = "Coping8349@outlook.com"
    MailServerPass = "na7yDLBdi7Qnw5"
     
    # Mail bericht
    MailOntvanger = "11901231@student.pxl.be"
    MailZender = "Coping8349@outlook.com"
    MailOnderwerp = "Login OctoPi"
    MailBericht = "Gebruikersnaam: " + 
     
    # Contact  maken met mailserver
    mailserver = smtplib.SMTP(MailServerAdres, MailServerPoort)
    mailserver.starttls() # TLS versleuteling nodig voor Hotmail/Gmail (werkt ook met Hostnet)
    mailserver.login(MailServerLogin, MailServerPass)
     
    # Bericht samenstellen
    bericht = 'To:' + MailOntvanger  + '\n' + 'From: ' + MailZender + '\n' + 'Subject:' + MailOnderwerp + '\n\n' + MailBericht + '\n\n'
     
    # Mail verzenden
    try:
      mailserver.sendmail(MailZender, MailOntvanger, bericht)
      print ("OK: email verzonden")
    except SMTPException:
      print ("FOUT: kan email niet verzenden!")



