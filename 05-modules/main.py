# Type these in the interpreter after creating calculator.py

# calculator # raises error
import calculator
calculator.__name__ # 'calculator'
calculator.sum(2, 3) # 5

sum = calculator.sum
sum(2, 3) # 5

from calculator import sum
sum(2, 3) # 5
calculator # raises error

from calculator import * # imports all names except those beginning with an underscore, dangerous
sum(2, 3) # 5

import calculator as calc
calc.sum(2, 3)

from calculator import sum as add
add(2, 3)

# Python looks for a built-in module, then a local file. Built-in module names are:
import sys
sys.builtin_module_names
# ('_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io',
#  '_locale', '_operator', '_signal', '_sre', '_stat', '_string', '_symtable',
#  '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 'builtins',
#  'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd',
#  'sys', 'time', 'xxsubtype')

# Local files are searched in the following directories:
sys.path
# ['', '/usr/lib/python310.zip', '/usr/lib/python3.10',
#  '/usr/lib/python3.10/lib-dynload', '/usr/lib/python3.10/site-packages']

# Speaking of sys, let's read and change primary and secondary prompts:

sys.ps1
sys.ps2
sys.ps1 = 'Type here: > '
sys.ps2 = 'Continued... '

import calculator, sys # import multiple modules in the same line

# Check names defined by modules
dir(calculator) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sum']
dir(sys) # a long list of names
dir() # all names currently defined

# dir() doesn't list the names of built-in functions and variables, this does:

import builtins
dir(builtins)