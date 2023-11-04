name = 'Antony'
language = 'Python'
f'My name is {name} and I <3 {language.upper()}!'

'My name is {} and I <3 {}!'.format('Antony', 'Python')
'My name is {1} and I <3 {0}!'.format(name, language.upper())
'My name is {name} and I <3 {language}!'.format(name=name, language=language.upper())

othree = 0.1 + 0.2
othree # 0.30000000000000004
'{:.1}'.format(othree) # '0.3'
float('{:1.1}'.format(othree)) # 0.3
'{:.17}'.format(othree) # '0.30000000000000004'

pi = 22 / 7
pi # 3.142857142857143
'{:.2}'.format(pi) # '3.1' ???
'{:.2f}'.format(pi) # '3.14'

# For extra features of format @see https://www.w3schools.com/python/ref_string_format.asp

str(22 / 7) # converts anything to string
repr(22 / 7) # same
repr('Hello world!') # returns a string representing the string: "'Hello world!'"

f'The approx value of pi is {22 / 7:.2f}'