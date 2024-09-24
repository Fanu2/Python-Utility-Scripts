import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = 'you@example.com'
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('you@example.com', 'password')
        server.send_message(msg)

send_email('Test Subject', 'This is a test email body.', 'friend@example.com')
