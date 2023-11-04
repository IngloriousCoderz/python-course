# All of this...

f = None
try:
  f = open('myfile.txt', 'r')
  print(f.read())
except FileNotFoundError:
  print('File not found')
finally:
  if f is not None:
    print('Closing file...', end=' ')
    f.close()
    print('Done.')

# ... can be replaced by this

with open('myfile.txt') as f:
  print(f.read())
