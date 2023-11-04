def shout(message):
  return message.upper()

shout('hello world') #?

def add_punctuation(message, punctuation):
  return message + punctuation

add_punctuation('hello world', '!') #?

def wrap_in_tag(message, tagname):
  return f"<{tagname}>{message}</{tagname}>"

wrap_in_tag('hello world', 'div') #?

wrap_in_tag(add_punctuation(shout('hello world'), '!'), 'div') #?

wrap_in_tag(
  add_punctuation(
    shout(
      'hello world'
    ),
    '!'
  ),
  'div'
)

def add_punctuation(punctuation):
  return lambda message: message + punctuation

def wrap_in_tag(tagname):
  return lambda message: f"<{tagname}>{message}</{tagname}>"

add_exclamation = add_punctuation('!')
wrap_in_div = wrap_in_tag('div')

wrap_in_div(
  add_exclamation(
    shout(
      'hello world'
    )
  )
) #?

message = 'hello world'
message = shout(message)
message = add_exclamation(message)
message = wrap_in_div(message)
message #?

from functools import reduce

def pipe(*functions):
  def apply_next_function(acc, function):
    return lambda value: function(acc(value))
  
  return reduce(apply_next_function, functions, lambda x: x)

transform = pipe(shout, add_exclamation, wrap_in_div)
transform('hello world') #?

def compose(*functions):
  def apply_next_function(acc, function):
    return lambda value: acc(function(value))
  
  return reduce(apply_next_function, functions, lambda x: x)

transform = compose(wrap_in_div, add_exclamation, shout)
transform('hello world') #?
