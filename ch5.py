def is_positive(x):
    """ (number) -> bool
    
    Return True iff x is positive.
    
    >>> is_positive(3)
    True
    >>> is_positive(-4.6)
    False
    """
    return x > 0

# iff: if and only if

(2 < 3) or (1 / 0)

# Comparing strings
'A' < 'a'

'abc' < 'abd'

'abc' < 'abcd'

'Jan' in '01 Jan 1838'

date = input('Enter a date in the format DD MTH YYYY: ')

'Jan' in date

# in operator is case-sensitive
'A' in 'abc'

# empty string is always a substring of every string
'' in 'abc'

# if statements
ph = float(input('Enter the pH level: '))

if ph < 7.0:
    print(ph, 'is acidic.')
    print('You should be careful with that!')
    
    ph = float(input('Enter the pH level: '))

if ph < 7.0:
    print(ph, 'is acidic.')
elif ph > 7.0:
    print(ph, 'is basic.')
    

# multiple elifs
compound = input('Enter the compound: ')

if compound == 'H20':
    print('Water')
elif compound == 'NH3':
    print('Ammonia')
elif compound == 'CH4':
    print('Methane')
else:
    print('Unknown compound')
    
# nested if statements
value = input('Enter the pH level: ')
if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, 'is acidic.')
    elif ph > 7.0:
        print(ph, 'is basic.')
    else:
        print(ph, 'is neutral.')
else:
    print('No pH value was given!')
    
# translating decision tables into code
if age < 45:
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'

# simplify by creating a variable to represent bmi and age status
young = age < 45
slim = bmi < 22.0
if young:
    if slim:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if slim:
        risk = 'medium'
    else:
        risk = 'high'

# without nesting
young = age < 45
slim = bmi < 22.0
if young and slim:
    risk = 'low'
elif young and not slim:
    risk = 'medium'
elif not young and slim:
    risk = 'medium'
elif not young and not slim:
    risk = 'high'
    


    

    
