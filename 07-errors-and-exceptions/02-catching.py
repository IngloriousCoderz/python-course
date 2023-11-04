# number = int(input('Please enter a number: ')) # raises ValueError for non-numbers

number = None
while number is None:
  try:
    number = int(input('Please enter a number: '))
  except ValueError:
    print("Oops, that's not a number!")

print('Your number is ', number)

# Catching multiple exceptions at once

try:
  pass
except (RuntimeError, TypeError, NameError):
  pass

# Catching exceptions individually

try:
  f = open('myfile.txt')
  s = f.readline()
  i = int(s.strip())
  print(i)
except FileNotFoundError as err:
  print('File not found', err)
except ValueError as err:
  print('Could not convert value to int', err)
except BaseException as err:
  print(f"Unexpected {err=}, {type(err)=}")


# The else clause is executed after the try if no exception was raised, Python-only

try:
  f = open('myfile.txt', 'r')
except OSError:
  print('Cannot open file')
else:
  print('File has', len(f.readlines()), 'lines')
  f.close()

# For extra exception features @see https://docs.python.org/3/tutorial/errors.html