import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email"
sender = "jo.sluft@gmail.com"
receiver = "lbsobreira@gmail.com"
password = input("Enter a password: ")

message = EmailMessage()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()  # context to a secure connection

print("Sending Email!")
# connect to the secure socket layer
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("Success!")
