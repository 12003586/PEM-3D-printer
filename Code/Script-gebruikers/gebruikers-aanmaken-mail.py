# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage

# set your email and password
# please use App Password
email_address = "Coping8349@outlook.com"
email_password = "na7yDLBdi7Qnw5"

# create email
msg = EmailMessage()
msg['Subject'] = "Email subject"
msg['From'] = email_address
msg['To'] = "11901231@student.pxl.be"
msg.set_content("This is eamil message")

# send email
with smtplib.SMTP_SSL('smtp.office365.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)