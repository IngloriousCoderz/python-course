def sum(a, b):
  if a is None:
    raise ValueError('You should give a value to the first parameter')
  if b is None:
    raise ValueError('You should give a value to the second parameter')
  return a + b

sum(41, None)

try:
  raise NameError('What an ugly name!')
except NameError as error:
  print(error)
  raise # try with and without raising

# Exception chaining

try:
  raise NameError('What an ugly name!')
except NameError as error:
  raise RuntimeError('Script exploded') from error

# Some exceptions are chained by default

try:
  open('myfile.txt')
except OSError:
  raise RuntimeError from None # prevents chaining

try:
  while True:
    print('Hello world!')
except KeyboardInterrupt:
  print('Did you press Ctrl-C?')
  raise
finally:
  print('Goodbye world!')

print('Hello again!')
