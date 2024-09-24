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
