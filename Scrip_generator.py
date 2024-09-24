import os

# Define the project path and scripts path
project_path = '/home/jasvir/PycharmProjects/Top50AutomationScripts'
scripts_path = os.path.join(project_path, 'scripts')

# List of additional 20 scripts
additional_scripts = {
    'stock_price_fetcher.py': """\
import requests

def fetch_stock_price(symbol):
    url = f'https://api.example.com/stocks/{symbol}'
    response = requests.get(url)
    data = response.json()
    return data['price']

symbol = 'AAPL'
price = fetch_stock_price(symbol)
print(f'The price of {symbol} is ${price}')
""",
    'git_repo_cloner.py': """\
import subprocess

def clone_repo(repo_url, destination):
    subprocess.run(['git', 'clone', repo_url, destination])

repo_url = 'https://github.com/username/repository.git'
destination = '/path/to/destination'
clone_repo(repo_url, destination)
""",
    'text_file_word_count.py': """\
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

file_path = 'sample.txt'
word_count = count_words(file_path)
print(f'The file contains {word_count} words')
""",
    'json_formatter.py': """\
import json

json_data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''

data = json.loads(json_data)
formatted_json = json.dumps(data, indent=4)
print(formatted_json)
""",
    'data_cleaner.py': """\
import pandas as pd

data = pd.read_csv('data.csv')
cleaned_data = data.dropna()
cleaned_data.to_csv('cleaned_data.csv', index=False)
""",
    'smtp_email_sender.py': """\
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
""",
    'file_compressor.py': """\
import zipfile

def compress_file(file_path, output_path):
    with zipfile.ZipFile(output_path, 'w') as zipf:
        zipf.write(file_path, os.path.basename(file_path))

file_path = 'example.txt'
output_path = 'example.zip'
compress_file(file_path, output_path)
""",
    'file_extractor.py': """\
import zipfile

def extract_file(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

zip_path = 'example.zip'
extract_to = 'extracted_files'
extract_file(zip_path, extract_to)
""",
    'api_data_post.py': """\
import requests

data = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=data)
print(response.status_code)
print(response.json())
""",
    'url_checker.py': """\
import requests

def check_url(url):
    response = requests.get(url)
    return response.status_code

url = 'https://example.com'
status = check_url(url)
print(f'The status code for {url} is {status}')
""",
    'file_content_replacer.py': """\
def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_text, new_text)

    with open(file_path, 'w') as file:
        file.write(content)

file_path = 'example.txt'
replace_text_in_file(file_path, 'old_text', 'new_text')
""",
    'json_to_csv.py': """\
import json
import csv

json_file = 'data.json'
csv_file = 'data.csv'

with open(json_file, 'r') as jf:
    data = json.load(jf)

with open(csv_file, 'w', newline='') as cf:
    writer = csv.writer(cf)
    writer.writerow(data[0].keys())
    for item in data:
        writer.writerow(item.values())
""",
    'api_data_put.py': """\
import requests

data = {'key': 'new_value'}
response = requests.put('https://api.example.com/data/1', json=data)
print(response.status_code)
print(response.json())
""",
    'website_status_checker.py': """\
import requests

def check_website_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f'{url} is up!')
    except requests.exceptions.RequestException as e:
        print(f'{url} is down! Error: {e}')

url = 'https://example.com'
check_website_status(url)
""",
    'rss_feed_reader.py': """\
import feedparser

rss_url = 'http://example.com/rss'
feed = feedparser.parse(rss_url)

for entry in feed.entries:
    print(entry.title)
    print(entry.link)
    print(entry.summary)
""",
    'contact_list_exporter.py': """\
import csv

contacts = [
    {'Name': 'John Doe', 'Email': 'john@example.com'},
    {'Name': 'Jane Doe', 'Email': 'jane@example.com'}
]

with open('contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for contact in contacts:
        writer.writerow(contact)
""",
    'pdf_to_text.py': """\
from PyPDF2 import PdfFileReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

pdf_path = 'sample.pdf'
text = extract_text_from_pdf(pdf_path)
print(text)
""",
    'html_table_to_csv.py': """\
import pandas as pd

html_file = 'table.html'
csv_file = 'table.csv'

tables = pd.read_html(html_file)
df = tables[0]
df.to_csv(csv_file, index=False)
""",
    'image_to_grayscale.py': """\
from PIL import Image

def convert_to_grayscale(image_path, output_path):
    with Image.open(image_path) as img:
        gray_img = img.convert('L')
        gray_img.save(output_path)

convert_to_grayscale('input.jpg', 'grayscale.jpg')
""",
    'weather_forecast.py': """\
import requests

api_key = 'your_api_key'
city = 'New York'
url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

for forecast in data['list']:
    print(f"Date: {forecast['dt_txt']}")
    print(f"Weather: {forecast['weather'][0]['description']}")
    print(f"Temperature: {forecast['main']['temp']}K")
    print()
""",
    'text_file_combiner.py': """\
import os

def combine_text_files(directory, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(directory):
            if filename.endswith('.txt'):
                with open(os.path.join(directory, filename), 'r') as infile:
                    outfile.write(infile.read() + '\\n')

combine_text_files('/path/to/directory', 'combined.txt')
""",
    'currency_converter.py': """\
import requests

def convert_currency(amount, from_currency, to_currency):
    api_url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(api_url)
    rates = response.json()['rates']
    return amount * rates[to_currency]

amount = 100
from_currency = 'USD'
to_currency = 'EUR'
converted_amount = convert_currency(amount, from_currency, to_currency)
print(f'{amount} {from_currency} is {converted_amount} {to_currency}')
""",
    'text_file_sorter.py': """\
def sort_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines.sort()

    with open(file_path, 'w') as file:
        file.writelines(lines)

file_path = 'example.txt'
sort_file(file_path)
""",
    'json_data_merger.py': """\
import json

def merge_json_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    merged_data = data1 + data2

    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)

merge_json_files('file1.json', 'file2.json', 'merged.json')
""",
    'weather_alert.py': """\
import requests

def get_weather_alert(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    data = response.json()

    if data['weather'][0]['main'] in ['Storm', 'Rain']:
        return f"Weather alert for {city}: {data['weather'][0]['description']}"
    return None

api_key = 'your_api_key'
city = 'New York'
alert = get_weather_alert(api_key, city)
if alert:
    print(alert)
""",
    'youtube_video_downloader.py': """\
from pytube import YouTube

def download_video(url, path):
    yt = YouTube(url)
    ys = yt.streams.get_highest_resolution()
    ys.download(path)

video_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
download_video(video_url, '/path/to/download')
"""
}

# Write additional scripts to files
for script_name, script_content in additional_scripts.items():
    with open(os.path.join(scripts_path, script_name), 'w') as f:
        f.write(script_content)

print("Additional scripts added successfully.")
