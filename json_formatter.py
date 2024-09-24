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
