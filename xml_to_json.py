import xmltodict
import json

xml_data = '''
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
'''

data_dict = xmltodict.parse(xml_data)
json_data = json.dumps(data_dict, indent=4)
print(json_data)
