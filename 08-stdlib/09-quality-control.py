from typing import Iterable


def average(values: Iterable[float]) -> float:
  """
  Computes the arithmetic mean of a sequence of numbers.
  
  >>> print(average([20, 30, 70]))
  40.0

  # >>> print(average([20, 30, 50]))
  # 40.0
  """
  return sum(values) / len(values)

import doctest
doctest.testmod()

# Try executing the script and then changing 40.0 to 50.0

# There are other testing tools, @see https://www.softwaretestinghelp.com/python-testing-frameworks/
