def add(a, b):
  return a + b

add(2, 3) #?
add(2, 8) #?

def add(a):
  def inner_function(b):
    return a + b
  
  return inner_function

def add(a):
  return lambda b: a + b

add = lambda a: lambda b: a + b

add_two = add(2) #?
add_two(3) #?
add_two(8) #?
