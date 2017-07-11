# Processing items in a list
velocities = [0.0, 9.81, 19.62, 29.43]
print('Metric:', velocities[0], 'm/sec;',
      'Imperial:', velocities[0] * 3.28, 'ft/sec')

print('Metric:', velocities[1], 'm/sec;',
      'Imperial:', velocities[1] * 3.28, 'ft/sec')

print('Metric:', velocities[2], 'm/sec;',
      'Imperial:', velocities[2] * 3.28, 'ft/sec')

print('Metric:', velocities[3], 'm/sec;',
      'Imperial:', velocities[3] * 3.28, 'ft/sec')

# use for loop
for velocity in velocities:
    print('Metric:', velocity, 'm/sec;',
          'Imperial:', velocity * 3.28, 'ft/sec')

speed = 2
for speed in velocities:
    print('Metric:', speed, 'm/sec')
print('Final:', speed)

# since existing variable is used, content of speed variable prior to loop is lost

# Chapter 9.2
# Processing Character in Strings

# loop over characters of string
country = 'United States of America'
for ch in country:
    if ch.isupper():
        print(ch)

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

# Chapter 9.4
# Processing Lists using indices
values = [4, 10, 3, 8, -6]
for num in values:
    num = num * 2

values # doubling values inside loop does not mutate list

len(values)    # 5

list(range(5))    # [0, 1, 2, 3, 4]

list(range(len(values)))    # [0, 1, 2, 3, 4]

# loop over indices of the list
for i in range(len(values)):
    print(i)

# use index to access items in list
for i in range(len(values)):
    print(i, values[i])

# use index to modify list items
for i in range(len(values)):
    values[i] = values[i] * 2
    
# processing parallel lists using indices
metals = ['Li', 'Na', 'K']
weights = [6.941, 22.98976928, 39.0983]

for i in range(len(metals)):
    print(metals[i], weights[i])

# Chapter 9.5
# Nesting loops in loops

outer = ['Li', 'Na', 'K']
inner = ['F', 'Cl', 'Br']
for metal in outer:
    for halogen in inner:
        print(metal + halogen)

# Create a multiplication table
def print_talbe(n):
    """ (int) -> NoneType
    
    Print the multiplication table for numbers 1 through n inclusive.
    
    >>> print_table(5)
        1    2    3    4    5
    1   1    2    3    4    5
    2   2    4    6    8    10
    3   3    6    9    12   15
    4   4    8    12   16   20
    5   5    10   15   20   25
    """
    
    # The numbers to include in the table.
    numbers = list(range(1, n + 1))
    
    # Print the header row.
    for i in numbers:
        print('\t' + str(i), end='')
    
    # End the header row.
    print()
    
    # Print each row number and the contents of each row.
    for i in numbers:
        
        print(i, ends='')
        for j in numbers:
            print('\t' + str(i * j), ends='')
        
        # End the current row.
        print()
        
# Looping over nested lists
elements = [['Li', 'Na', 'K'], ['F', 'Cl', 'Br']]
for inner_list in elements:
    print(inner_list)
    
# access each string in inner lists
for inner_list in elements:
    for item in inner_list:
        print(item)
        
# Looping over ragged lists (nested lists with inner lists of varying lengths)
info = [['Isaac Newton', 1643, 1727],
        ['Charles Darwin', 1809, 1882],
        ['Alan Turing', 1912, 1954, 'alan@bletchley.uk']]
for item in info:
    print(len(item))


drinking_times_by_day = [['9:02', '10:17', '13:52', '18:23', '21:31'],
                         ['8:45', '12:44', '14:52', '22:17'],
                         ['8:55', '11:11', '12:34', '13:46', '15:52', '17:08'],
                         ['9:15', '11:44', '16:28']]

for day in drinking_times_per_day:
    for drinking_time in day:
        print(drinking_time, end=' ')
    print()


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

# Chapter 9.7
# Repetition based on user input
text = ''
while text != 'quit':
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("..exiting program")
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")

# Chapter 9.8
# Controlling loops using break and continue

# break: terminates execution of loop immediately
# continue: skip ahead to next iteration

while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("..exiting program")
        break
    elif text == "H2O":
        print("Water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("Methane")
    else:
        print("Unknown compound")
        
# find index of first digit in string 'C3H7'
s = 'C3H7'
digit_index = -1 # This will be -1 until we find a digit.
for i in range(len(s)):
    # If we haven't found a digit, and s[i] is a digit
    if digit_index == -1 and s[i].isdigit():
        digit_index = i
        break # This exits the loop.
        
digit_index

# the continue statement
s = 'C3H7'
total = 0 # The sum of the digits seen so far.
count = 0 # The number of digits seen so far.
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = totla + int(s[i])
    couunt = count + 1
    
total
count

# using if statements
s = 'C3H7'
total = 0
count = 0
for i in range(len(s)):
    if not s[i].isalpha():
        total = total + int(s[i])
        count = count + 1

# most of the time it is better to avoid continue
# break and continue should be used sparingly

