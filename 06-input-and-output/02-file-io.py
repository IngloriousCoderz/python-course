f = open('students.csv', 'r', encoding="utf-8")
data = f.read()
print(data) # Harry,Potter
            # Hermione,Granger
            # Ron,Weasley
f.close()
f.closed # checks if the file was closed

# Second argument available values:
# r - read
# w - write
# a - append
# r+ - read and write
# no value - read-only by default

f = open('students.csv', 'rb') # read as binary file
data = f.read()
print(data) # b'Harry,Potter\nHermione,Granger\nRon,Weasley\n'
f.close()

# What is 'with'? @see https://stackoverflow.com/a/1369553/12491045

with open('students.csv', encoding='utf-8') as f:
  data = f.read()
  print(data)
f.closed # returns True without explicitly closing
f.read() # raises an error: file was already closed

list(f) # reads all lines as a list: ['Harry,Potter\n', 'Hermione,Granger\n', 'Ron,Weasley\n']
f.readlines() # same as above

f.readline() # reads one line at a time

for line in f:
  print(line, end='')

with open('students.csv', 'a', encoding='utf-8') as f:
  f.write('Neville,Longbottom\n') # writes the line and returns number of characters written
