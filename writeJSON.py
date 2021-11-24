import json 

#the json library does not need to be preinstalled

#key, value pair will turn into json field name and data

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)