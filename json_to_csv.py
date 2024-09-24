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
