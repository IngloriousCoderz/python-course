# @see https://www.datacamp.com/tutorial/making-http-requests-in-python

import requests # installed via pip

response = requests.get('https://swapi.dev/api/people/1/')
print(response.status_code)
print(response.headers)
print(response.json())

response = requests.post('https://swapi.dev/api/people/', json={'name': 'Antony'})
print(response.status_code)
print(response.headers)
print(response.json())
