import smtplib

# Server instellingen
MailServerAdres = "smtp.office365.com"
MailServerPoort = "587"
MailServerLogin = "Octoprint@outlook.be"
MailServerPass = "na7yDLBdi7Qnw5"
 
# Mail bericht
MailOntvanger = "11901231@student.pxl.be"
MailZender = "Octoprint@outlook.be"
MailOnderwerp = "Login OctoPi"
MailBericht = "Testing: Mail"
 
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

