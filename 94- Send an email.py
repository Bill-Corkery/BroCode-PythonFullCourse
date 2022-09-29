#Lesson 94: Send an email
# https://www.youtube.com/watch?v=xiUTqnI6xk8

import smtplib

send = 'sender@gmail.com'  #use own email
receiver = 'receiver@gmail.com'
password = 'password123'
subject = 'python email test'
body = 'I wrote an email'

message = f"""From: Python test{sender}
To: Receiver{receiver}
Subject: {subject}\n
{body}
"""
server = smtplib.SMTP("smtp.gmail.com", 587)  #587 is default mail submission port.
server.starttls()

try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
    #may ecounter SMTPAuthenticationError. this means username and password were not accepted OR
    # need to turn on less secure on gmail.
except smtplib.SMTPAuthenticationError:
    print('Unable to sign in')