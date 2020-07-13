import os
import smtplib
from email.message import EmailMessage
Email_Addr = '<Sender's Mail>'
Email_pass = '<Password>'
msg = EmailMessage()
msg['Subject'] = "Test Failed"
msg['From'] = Email_Addr
msg['To'] = "<Receiver's Mail>"
msg.set_content("New Update in Website has FAILED the test")
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(Email_Addr, Email_pass)
    smtp.send_message(msg)
