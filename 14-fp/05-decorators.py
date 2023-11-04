def say_hello():
  return 'Hello world!'

print('Logging no-arg function:')

def add_logging(func):
  print('Before function...')
  result = func()
  print('After function.')
  return result

print(add_logging(say_hello))

print('Logging function with args:')

def subtract(a, b):
  return a - b

def add_logging(func, *args):
  print('Before function...')
  result = func(*args)
  print('After function.')
  return result

print(add_logging(subtract, 2, 3))

print('Logging with currying:')

def add(a, b):
  return a + b

def add_logging(func):
  def inner_func(*args):
    print('Before function...')
    result = func(*args)
    print('After function.')
    return result
  
  return inner_func

subtract_with_logging = add_logging(subtract)
print(subtract_with_logging(2, 3))
print(subtract_with_logging(17, 12))

add_with_logging = add_logging(add)
print(add_with_logging(2, 3))
print(add_with_logging(17, 12))

print('Decorator:')

@add_logging
def subtract(a, b):
  return a - b

print(subtract(2, 3))

print('Cached results:')

from functools import cache

@cache
def factorial(n):
  print('Computing factorial of', n)
  return n * factorial(n - 1) if n > 2 else 2

print('Recursive factorial of 5:', factorial(5))
print('Recursive factorial of 3:', factorial(3))
print('Recursive factorial of 7:', factorial(7))
