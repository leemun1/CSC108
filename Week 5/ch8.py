whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
whales

# list is an object
whales[0]
whales[12]

whales[1001] # index out of range

whales[-1] # last index
whales[-2] # one index before last

# assign list item to other variable
third = whales[2]

print('Third day:', third)

# emptry list
whales = []

whales[0] # error; list has no item

# lists can contain any type of data
krypton = ['Krypton', 'Kr', -157.2, 153.4]
krypton[1]
krypton[2]

# modifying lists; list objects are mutable
nobles = ['helium', 'none', 'argon', 'krypton', 'xenon', 'radon']

nobles[1] = 'neon'
nobles

# numbers and strings are immutable; methods actually create new strings
name = 'Darwin'
capitalized = name.upper()
print(capitalized)
print(name)

# operation on lists
half_lives = [887.7, 24100.0, 6503.0, 14, 373300.0]
len(half_lives)
max(half_lives)
min(half_lives)
sum(half_lives)
sorted(half_lives)
half_lives

# comining lists; creates new list
original = ['H', 'He', 'Li']
final = original + ['Be']
final

# cannot concatenate list and string
['H', 'He', 'Li'] + 'Be' # error

# multiply list; repeated items
metals = ['Fe', 'Ni']
metals * 3

# delete item from a list
del metals[0]

# the 'in' operator
nobles = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
gas =input('Enter a gas: ')

if gas in nobles:
    print('{} is noble'.format(gas))
    
# in operator cannot check for sublists
[1, 2] in [0, 1, 2, 3] # error

# slicing lists
celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Lon', 'Dpy', 'Sma']

useful_markers = celegans_phenotypes[0:4] # from 0 upto, but not including 4

# first index can be omitted if slicing from front
# last index can be ommited if slicing to end

celegans_phenotypes[:4]
celegans_phenotypes[4:]

# omit both indices to create copy of list
celegans_copy = celegans_phenotypes[:]

# Aliasing
celegans_alias = celegans_phenotypes
celegans_phenotypes[5] = 'Lvl'
celegans_phenotypes
celegans_alias

# aliasing list can be dangerous because lists are mutable
# safe with immutable types

# mutable parameters
def remove_last_item(L):
    """ (list) -> list
    
    Return list L with the last item removed.
    
    Precondition: len(L) >= 0
    
    >>> remove_last_item([1, 3, 2, 4])
    [1, 3, 2]
    """
    del L[-1]

# List methods
colors = ['red', 'orange', 'green']
colors.extend(['black', 'blue'])

colors.append('purple')

colors.insert(2, 'yellow')

colors.remove('black')

# Working with a list of lists
life = [['Canada', 76.5], ['United States', 75.5], ['Mexico', 72.0]]

life[0]
life[1]
life[2]

life[1][0]
life[1][1]

# assign sublists to variables
canada = life[0]
canada[0]
canada[1]

# assigning a subset to variable creates alias; changes made through sublist 
# is reflected on main list

canada[1] = 80.0
canada
life

# Chapter 9.3
# Looping over range of numbers

# generate sequence of integers
range(10) # range type

for num in range(10):
    print(num)

# create a list of such numbers
list(range(10))

# empty list
list(range(0))

# pass arguments for range()
list(range(1,5))

list(range(5, 10))

# specify different step size
list(range(2000, 2050, 4))
list(range(2050, 2000, -4)) # if step size < 0, starting index should be larger

# loop over sequence
total = 0
for i in range(1, 101):
    total = total + i
    
total


# Chapter 9.6
# Looping until a condition is reached

# use while when dont know how many iterations
rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits = rabbits - 1
    
# calculate growth of bacterial colony
time = 0
population = 1000   # 1000 bacteria to start with
growth_rate = 0.21  # 21% growth per minute
while population < 2000:
    population = population + growth_rate * population
    print(round(population))
    time = time + 1

print ("It took", time, "minutes for the bacteria to double.")
print("The final population was", round(population), "bacteria.")

# infinite loops
""" if 'while population != 2000:', the loop never stops because population 
is never exactly 2000
"""