import json

person = {'name': 'Antony', 'date_of_birth': '1982-10-17', 'legs': ['left', 'right']}

string = json.dumps(person) # serializes to string
string # '{"name": "Antony", "date_of_birth": "1982-10-17", "legs": ["left", "right"]}'

person = json.loads(string) # deserializes from string
person # {'name': 'Antony', 'date_of_birth': '1982-10-17', 'legs': ['left', 'right']}

with open('db.json', 'w', encoding='utf-8') as f:
  json.dump(person, f) # serializes to file

with open('db.json', 'r', encoding='utf-8') as f:
  person = json.load(f) # deserializes from file
  print(person)
