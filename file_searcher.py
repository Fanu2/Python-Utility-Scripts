import os

search_directory = '/path/to/directory'
file_extension = '.txt'

for root, dirs, files in os.walk(search_directory):
    for file in files:
        if file.endswith(file_extension):
            print(os.path.join(root, file))
