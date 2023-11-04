def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

operands = [(2, 3), (3, -5), (42, 39)]

result = [add(a, b) for a, b in operands]
result #?

result = [subtract(a, b) for a, b in operands]
result #?

def perform_calculation(calculation, operands):
  return [calculation(a, b) for a, b in operands]

perform_calculation(add, operands) #?
perform_calculation(subtract, operands) #?
