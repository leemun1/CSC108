# defining function
def convert_to_celsius(farenheit):
    return (farenheit - 32) * 5 / 9

# using local variables for temporary storage
def quadratic(a, b, c, x):
    first = a * x ** 2
    second = b * x
    third = c
    return first + second + third

# call quadratic()
print(quadratic(2, 3, 4, 0.5))

# Example function with docstring
def days_difference(day1, day2):
    """ (int, int) -> int 
    
    Return the number of days between day1 and day2, which are
    both in the range 1-365 (thus indicating the day of the year).
    
    >>> days_difference(200, 224)
    24
    >>> days_difference(50, 50)
    0
    >>> days_difference(100, 99)
    -1
    """
    return day2 - day1

# the first line : function header

# the second line: describe types of values to be passed and returned

# after that: decription of what the function will do when called; 
# mention parameters and describe what the function returns

# after that: example calls and return values as expected

# after that: body of function

def get_weekday(current_weekday, days_ahead):
    """ (int, int) -> int
    
    Return which day of the week it will be days_ahead days 
    from current_weekday.
    
    current_weekday is the current day of the week and is in the range
    1-7, indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).
    
    days_ahead is the number of days after today.
    
    >>> get_weekday(3, 1)
    4
    >>> get_weekday(6, 1)
    7
    >>> get_weekday(7, 1)
    1
    >>> get_weekday(1, 0)
    1
    >>> get_weekday(4, 7)
    4
    >>> get_weekday(7, 72)
    2
    """
    return (current_weekday + days_ahead - 1) % 7 + 1

def get_birthday_weekday(current_weekday, current_day, birthday_day):
    """ (int, int, int) -> int
    
    Return the day of the week it will be on birthday_day, given that the
    day of the week is current_weekday and the day of the year is
    current_day.
    
    current_weekday is the current day of the week and is in the range 1-7,
    indicating whether today is Sunday (1), Monday (2), ..., Saturday (7).
    
    current_day and birthday_day are both in the range 1-365.
    
    >>> get_birthday_weekday(5, 3, 4)
    6
    >>> get_birthday_weekday(5, 3, 116)
    6
    >>> get_birthday_weekday(6, 116, 3)
    5
    """
    days_diff = days_difference(current_day, birthday_day)
    return get_weekday(current_weekday, days_diff)

def pie_percent(n):
    """ (int) -> int
    
    Precondition: n > 0
    
    Assuming there are n people who want to eat a pie, return the percentage
    of the pie that each person gets to eat.
    
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """
    
    return int(100/n)


    
    