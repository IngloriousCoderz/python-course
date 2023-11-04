def speak(self):
  return f"Hi! My name is {self['first_name']} and I have {self['legs']} legs."

person = {
  'first_name': 'Matteo Antony',
  'last_name': 'Mistretta',
  'date_of_birth': '1982-10-17',
  'speak': speak,
  'legs': 2
}
person['speak'](person) #?

another_person = {
  'first_name': 'George',
  'last_name': 'Jetson',
  'date_of_birth': '2022-08-22',
  'speak': speak,
  'legs': 2
}
another_person['speak'](another_person) #?
another_person['speak'](person) #?