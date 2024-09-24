import subprocess

def clone_repo(repo_url, destination):
    subprocess.run(['git', 'clone', repo_url, destination])

repo_url = 'https://github.com/username/repository.git'
destination = '/path/to/destination'
clone_repo(repo_url, destination)
