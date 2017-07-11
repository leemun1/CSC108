import tweet
import builtins

# Get the initial value of the constant
constant_1_before = [50]
constant_2_before = ['@']

# Type check tweet.contains_googl_url
result = tweet.contains_googl_url('Test 123')
assert isinstance(result, bool), \
       '''tweet.contains_googl_url should return a bool, but returned {0}
       .'''.format(type(result))

# Type check tweet.add_mention
result = tweet.add_mention('Test 123', 'a').strip()
assert isinstance(result, str), \
       '''tweet.add_mention should return a str, but returned {0}
       .'''.format(type(result))
assert result == 'Test 123 @a', \
       '''tweet.add_mention should return 'Test 123 @a', but returned '{0}'
       .'''.format(result)

# Type check tweet.min_tweets_required
result = tweet.min_tweets_required('Test 123')
assert isinstance(result, int), \
       '''tweet.min_tweets_required should return an int, but returned {0}
       .'''.format(type(result))

# Type check tweet.is_mentioned
result = tweet.mentions_user('Test 123', 'abc')
assert isinstance(result, bool), \
       '''tweet.mentions_user should return a bool, but returned {0}.''' \
       .format(type(result))

# Type check tweet.report_shorter
result = tweet.report_shorter('abc', 'def')
assert isinstance(result, str), \
       '''tweet.report_shorter should return a str, but returned {0}.''' \
       .format(type(result))

# Type check tweet.create_reply_to
result = tweet.create_reply_to('abcd', 'def')
assert isinstance(result, str), \
       '''tweet.create_reply_to should return a str, but returned {0}.''' \
       .format(type(result))

# Get the final values of the constants
constant_1_after = [tweet.MAX_TWEET_LENGTH]
constant_2_after = [tweet.AT_SYMBOL]

# Check whether the constants are unchanged.
assert constant_1_before == constant_1_after, \
       '''Your function(s) modified the value of constant MAX_TWEET_LENGTH
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    
assert constant_2_before == constant_2_after, \
       '''Your function(s) modified the value of constant AT_SYMBOL
       Edit your code so that the value of the constant is not 
       changed by your functions.'''
    

print("""

Huzzah! The simple checker program completed without error.

This means that the functions in tweet.py:
- are named correctly,
- take the correct number of arguments, and
- return the correct types.  

This does NOT mean that the functions are correct!

Be sure to thoroughly test your functions yourself before submitting.""")


# Check for use of functions print and input.

def disable_print(*args):
    raise Exception("You must not call built-in function print!")

def disable_input(*args):
    raise Exception("You must not call built-in function input!")

builtins.print = disable_print
builtins.input = disable_input