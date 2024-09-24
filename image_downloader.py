import requests

url = 'https://media.gettyimages.com/id/2123386063/photo/lilys-aging-skin.jpg?s=2048x2048&w=gi&k=20&c=xLCWbTRuVMOGJ7kT51qPIph16IUyqfKp8l7hF5EEDO4='
response = requests.get(url)

with open('image.jpg', 'wb') as f:
    f.write(response.content)
