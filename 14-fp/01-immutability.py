person = {'name': 'Matteo Antony', 'age': 39}

def impure_increase_age(person, amount):
  person['age'] += amount

previous_age = person['age'] #?
impure_increase_age(person, 7) #?
age = person['age'] #?
print(age > previous_age)

def pure_increase_age(person, amount):
  new_person = person.copy()
  new_person['age'] += amount
  return new_person

new_person = pure_increase_age(person, 7) #?
person['age'] #?
new_person['age'] #?
print(new_person == person)
