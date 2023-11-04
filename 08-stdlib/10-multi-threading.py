# 10 people
# 20 cars
# 30 computers
# 60 total

# 10 people, 20 cars, 30 computers
# people ok, 10 cars, 20 computers
# people ok, cars ok, 10 computers
# people ok, cars ok, computers ok
# 30 total

from threading import Thread
import random, time

numbers = range(1, 5)

def long_task(name):
  print(f'Starting task {name}...')
  delay = random.choice(numbers)
  time.sleep(delay)
  print(f'Task {name} done after {delay} seconds.')

# print('Starting long tasks...')
# for num in numbers:
#   long_task(num)
# print('All tasks ended.')

# Simple multi-threading: just wait for tasks to complete

# create some threads with a list comprehension
threads = [Thread(target=long_task, args=(num,)) for num in numbers] # args can be a tuple or any other sequence, such as list

print('Starting threads...')
for thread in threads:
  thread.start()
print('Waiting for threads to complete...')
for thread in threads:
  thread.join()
print('All done.')

# Collecting the results is trickier: we need to store results in a list

results = [None for _ in numbers]

def long_task(name):
  print(f'Starting task {name}...')
  delay = random.choice(numbers)
  time.sleep(delay)
  # results.append(name) doesn't work as expected
  index = name - 1
  results[index] = name
  print(f'Task {name} done after {delay} seconds.')

threads = [Thread(target=long_task, args=(i,)) for i in numbers]

print('Starting threads...')
for thread in threads:
  thread.start()
print('Waiting for threads to complete...')
for thread in threads:
  thread.join()
print('All done.')
print('Results:', results)

# A simpler and better way, taken from https://realpython.com/intro-to-python-threading/

from concurrent.futures import ThreadPoolExecutor

def long_task(name):
  print(f'Starting task {name}...')
  delay = random.choice(numbers)
  time.sleep(delay)
  print(f'Task {name} done after {delay} seconds.')
  return name

print(long_task('1'))

print('Starting threads with a pool...')
with ThreadPoolExecutor(max_workers = 4) as executor:
  results = executor.map(long_task, numbers)
print('All done.')
print('Results:', list(results))

# For more asynchronous I/O @see https://docs.python.org/3/library/asyncio.html
# For asynchronous HTTP @see https://docs.aiohttp.org/en/stable/
