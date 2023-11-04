# n! = 1 * 2 * ... * (n - 1) * n
# 5! = 1 * 2 * 3 * 4 * 5 = 120
# 3! = 1 * 2 * 3 = 6
# 7! = 1 * 2 * 3 * 4 * 5 * 6 * 7 = 5! * 6 * 7 = 5040

# 2! = 2
# 3! = 3 * 2!
# 4! = 4 * 3!
# 5! = 5 * 4!

def non_recursive_factorial(n):
  factorial = 1
  for num in range(2, n + 1):
    print('Multiplying', num)
    factorial *= num
  return factorial

print('Non-recursive factorial of 5:', non_recursive_factorial(5))
print('Non-recursive factorial of 3:', non_recursive_factorial(3))
print('Non-recursive factorial of 7:', non_recursive_factorial(7))

def recursive_factorial(n):
  print('Computing factorial of', n)
  return n * recursive_factorial(n - 1) if n > 2 else 2

print('Recursive factorial of 5:', recursive_factorial(5))
print('Recursive factorial of 3:', recursive_factorial(3))
print('Recursive factorial of 7:', recursive_factorial(7))
