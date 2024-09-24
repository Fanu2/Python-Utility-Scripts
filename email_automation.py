import smtplib
from email.mime.text import MIMEText

msg = MIMEText('This is the body of the email')
msg['Subject'] = 'Test Email'
msg['From'] = 'you@example.com'
msg['To'] = 'friend@example.com'

with smtplib.SMTP('smtp.example.com') as server:
    server.login('username', 'password')
    server.send_message(msg)
