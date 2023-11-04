class Person:
  legs = 2

  def __init__(self, first_name, last_name, date_of_birth):
    self.first_name = first_name
    self.last_name = last_name
    self.date_of_birth = date_of_birth

  def speak(self):
    return f"Hi! My name is {self.first_name} and I have {self.legs} legs."

person = Person('Matteo Antony', 'Mistretta', '1982-10-17')
person.speak() #?

another_person = Person('Geroge', 'Jetson', '2022-08-22')
another_person.speak() #?
# another_person.speak(person) # one argument passed, but it's seen as two #?

another_person.legs #?
Person.legs #?
another_person.speak #?
Person.speak #?
Person.__init__ #?
another_person.__init__ #?
Person.speak(another_person) #?
