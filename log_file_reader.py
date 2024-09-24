log_file_path = '/path/to/log/file.log'

with open(log_file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
