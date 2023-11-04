# Define this function, then go to main.py

def sum(a, b):
  return a + b

# After playing with main, promote this module to script as below

# Usage:
# python calculator.py 2 3

if __name__ == "__main__":
  import sys
  a = int(sys.argv[1])
  b = int(sys.argv[2])
  print(sum(a, b))

