from ftplib import FTP

ftp = FTP('ftp.example.com')
ftp.login(user='username', passwd='password')

filename = 'file.txt'
with open(filename, 'rb') as file:
    ftp.storbinary(f'STOR {filename}', file)

ftp.quit()
