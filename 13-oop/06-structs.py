class Row:
  def __init__(self, quantity, price):
    self.quantity = quantity
    self.price = price

  def calculate_amount(self):
    return self.quantity * self.price

class CashRegister:
  def __init__(self, rows):
    self.rows = rows

  def calculate_total(self):
    total = 0
    for row in self.rows:
      total += row.calculate_amount()
    return total

apples = Row(2, 1)
bananas = Row(3, 1.5)
cash_register = CashRegister([apples, bananas])
cash_register.calculate_total() #?
vars(cash_register) #?

rows = [{'quantity': 2, 'price': 1}, {'quantity': 3, 'price': 1.5}]

def calculate_amount(row):
    return row['quantity'] * row['price']

def calculate_total(rows):
  total = 0
  for row in rows:
    total += calculate_amount(row)
  return total

calculate_total(rows) #?

class Person:
  pass
  # later add this method:
  # def stringify(self):
  #   dictionary = vars(self)
  #   lines = [f"{key}: {value}" for key, value in dictionary.items()]
  #   return '\n'.join(lines)

person = Person()
person.first_name = 'Matteo Antony'
person.last_name = 'Mistretta'
person.date_of_birth = '1982-10-71'
person #?
vars(person) #?

def stringify(obj):
  dictionary = vars(obj)
  lines = [f"{key}: {value}" for key, value in dictionary.items()]
  return '\n'.join(lines)

print(stringify(person))
print(person.stringify()) #?

# For objections on OOP @see https://betterprogramming.pub/object-oriented-programming-the-trillion-dollar-disaster-92a4b666c7c7
# Also @see the referenced https://cscalfani.medium.com/goodbye-object-oriented-programming-a59cda4c0e53
