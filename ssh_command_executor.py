import paramiko

hostname = 'example.com'
username = 'your_username'
password = 'your_password'
command = 'ls'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

stdin, stdout, stderr = client.exec_command(command)
print(stdout.read().decode())

client.close()
