class Calculator:
  def sum(self, a=0, b=0): # instance method
    return a + b

calculator = Calculator()
calculator.sum(2, 3) #?

Calculator.sum(None, 2, 3) #?

class Calculator:
  def sum(a=0, b=0): # NOTE: we are not using 'self' anymore
    return a + b

Calculator.sum = staticmethod(Calculator.sum) # converted into a class method

Calculator.sum(2, 3) #?

class Calculator:
  @staticmethod # static method as a decorator, @see FP
  def sum(a=0, b=0):
    return a + b

Calculator.sum(2, 3) #?

# singleton

class Calculator:
  calculator = None

  @staticmethod
  def get_instance():
    if Calculator.calculator is None:
       Calculator.calculator = Calculator()
    return Calculator.calculator

calculator1 = Calculator.get_instance() #?
calculator2 = Calculator.get_instance() #?
print(calculator1 is calculator2) #?

# dependency injection

class Math:
  def __init__(self, calculator): # this instance will be injected by some DI framework
    pass
