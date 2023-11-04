person = {'name': 'Antony', 'date_of_birth': '1982-10-17', 'eyes': 2}
person['name'] # there is no dot notation, like 'person.name'
person['nose'] = 1 # add
person['nose'] = 2 # change
del person['nose'] # delete

list(person) # list of keys
sorted(person) # sorted list of keys
'name' in person # returns True

dict([('name', 'Antony'), ('date_of_birth', '1982-10-17'), ('eyes', 2)]) # build from list of tuples

# For extra features of dict @see https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

list(person.items()) # returns a list of tuples

for key in person:
  print(key)

# iterate over dictionary
for key, value in person.items():
  print(key, value)

# iterate over both index and item
for index, item in enumerate(['tic', 'tac', 'toe']):
  print(index, item)

# iterate over two collections
questions = ['name', 'favorite language', 'favorite color']
answers = ['Antony', 'JavaScript', 'indigo']

print(list(zip(questions, answers)))
for question, answer in zip(questions, answers):
  print(f"What is your {question}? It is {answer}")