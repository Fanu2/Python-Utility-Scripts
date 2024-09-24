import os

directory = '/path/to/directory'
for filename in os.listdir(directory):
    new_name = filename.replace('old', 'new')
    os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
