from functools import reduce

# reduce is used to accumulate a result, the most basic example is the summation of a sequence of numbers

def add(a, b):
  return a + b

# Procedural way:

total = 0
for num in range(1, 5):
  total = add(total, num) # same as total += num, but immutable
total #?

# Functional way:

total = reduce(add, range(1, 5), 0) #?

# We can use anything as an accumulator, even lists or dictionaries or functions.
# In fact we can implement map, filter and any other list functions with reduce:

def is_even(num):
  return num % 2 == 0

def append_if_even(acc, num):
  if is_even(num):
    acc = acc + [num] # same as acc.append(num), but immutable
  return acc

evens = []
for num in range(1, 5):
  evens = append_if_even(evens, num)
evens #?

evens = reduce(append_if_even, range(1, 5), [])
evens #?
