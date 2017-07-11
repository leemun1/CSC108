str.capitalize('browning')

# center given string in a string of length 26
str.center('Sonnet 43', 26) 

# count how many times 'the' occurs in given string
str.count('How do I love thee? Let me count the ways.', 'the')

# calling methods the OOP way; shorthand forms
'browning'.capitalize()

'Sonnet 43'.center(26)

'How do I love thee? Let me count the ways.'.count('the')

help(str.lower)

# any expression can be used as long as it evaluates to correct type
('TTA' + 'G' * 3).count('T')

'species'.startswith('a')

'species'.endsswith('spe')

# cleaning strings
compound = '     \n  Methyl \n butanol    \n'
compound.lstrip() # remove whitespace from front
compound.rstrip() # from end
compound.strip() # from both 

# swapcases
'Computer Science'.swapcase()

# use format() to subsitute series of strings into format string
'"{0}" is derived from "{1}"'.format('none', 'no one')
'"{0}" is derived form the {2} "{1}"'.format('December', 'decem', 'latin')

# use format() to specify num of decimal places to round
my_pi = 3.14159
'Pi rounded to {0} decimal places is {1:.2f}.'.format(2, my_pi)

# omit position numbers
'Pi rounded to {} decimal places is {:.3f}.'.format(2, my_pi)

# chaining methods
'Computer Science'.swapcase().endswith('ENCE')

# special methods with underscores
'TTA' + 'GGG'
'TTA'.__add__('GGG')

abs(-3)
-3 .__abs__() # space after -3 so that Python doesnt think it is a float

3 + 5
3 .__add__(5)

3 > 5
3 .__gt__(5)

abs.__doc__

# every function object keeps track of docstring in __doc__

# Chapter 9.2
# Processing Character in Strings

# loop over characters of string
country = 'United States of America'
for ch in country:
    if ch.isupper():
        print(ch)
        




