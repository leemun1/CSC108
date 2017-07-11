import math

# For this Assignment, the MAX_TWEET_LENGTH is smaller than 140 so as to
# simplify character counting and to avoid unnecessarily long strings.
MAX_TWEET_LENGTH = 50
AT_SYMBOL = '@'


# Add your own constants here, as needed



def contains_googl_url(tweet):
    """ (str) -> bool

    Return True if and only if tweet contains a link to an goo.gl URL of the
    form 'http://goo.gl/'.

    Assume tweet is a valid tweet.

    >>> contains_googl_url('Meetup on UX: http://goo.gl/6fo3df ')
    True
    >>> contains_googl_url('http://goo.gl/A4pm7n AI Seminar!')
    True
    >>> contains_googl_url('http://ow.ly/VGpA9 Team to transform U of T campus')
    False
    """

    # Complete this function body.
    if 'http://goo.gl/' in tweet:
        return True
    else:
        return False

# Now define the other functions described in the handout.
def add_mention(tweet, username):
    """ (str, str) -> str
    
    Attach the @ symbol to the username and append this to the end of the 
    original tweet to create a new 'mention' string.
    
    If total length of 'mention' string is at least 14 characters, return 
    'mention'. Otherwise, return the original tweet
    
    Assume tweet is a valid tweet.
    Assume username is a valid username.
    
    >>> add_mention('I like', 'csc108')
    'I like @csc108'
    >>> add_mention('Go talk to that guy', 'mikelee')
    'Go talk to that guy @mikelee'
    >>> add_mention('Test 123', 'a')
    'Test 123 @a'
    """
    
    # Create the mention string
    mention = tweet + ' ' + AT_SYMBOL + username
    
    # Examine string length and decide what to return
    if len(mention) <= MAX_TWEET_LENGTH:
        return mention
    else:
        return tweet

def mentions_user(tweet, username):
    """ (str, str) -> str
    
    Desc
    
    >>> mentions_user('I like @cssu', 'cssu')
    True
    >>> mentions_user('I like @cssu', 'css')
    False
    >>> mentions_user('Go talk to that guy @mikelee', 'kevin')
    False
    >>> mentions_user('Hey there @donkey', 'Donkey')
    False
    """
    if username == tweet[tweet.find('@') + 1:]:
        return True
    else:
        return False

def min_tweets_required(message):
    """ (str) -> int
    
    Returns minimum number of tweets required to post the message.
    
    >>> min_tweets_required("The type contracts have been included in the following table")
    2
    >>> min_tweets_required("The first parameter represents a valid username or a valid username preceded by @, and the second parameter represents a valid tweet. Prepare a reply tweet to the given username.")
    4
    """
    return (len(message) // MAX_TWEET_LENGTH) + 1

def report_shorter(tweet1, tweet2):
    """ (str, str) -> str
    
    Returns a string indicating the shorter tweet between tweet1 and tweet2. 
    
    If the two are of the same length, return 'Same length'
    
    >>> report_shorter("Spelled and capitalized", "here")
    'Tweet 2'
    >>> report_shorter("Mike", "studying csc108")
    'Tweet 1'
    >>> report_shorter("Apple", "House")
    'Same length'
    """
    
    if len(tweet1) < len(tweet2):
        return 'Tweet 1'
    elif len(tweet1) > len(tweet2):
        return 'Tweet 2'
    else:
        return 'Same length'

def create_reply_to(username, tweet):
    """ (str, str) -> str
    
    Returns a reply tweet which consists of a mention of the username
    followed by a space and the given tweet.
    
    If reply tweet is at most 140 characters long, return it.
    Otherwise, return a string indicating how many extra characters are in it.
    
    >>> create_reply_to("@Mikeleeinthehouse", "The first parameter represents a valid username or a valid username preceded by @, and the second parameter represents a valid tweet.")
    >>> create_reply_to("Trump", "Hey there Obama here")
    """
    reply = ''
    
    if '@' in username:
        reply = username + ' ' + tweet
    else:
        reply = '@' + username + ' ' + tweet        
        
    if len(reply) <= 140:
        return reply
    else:
        extra = len(reply) - 140
        return str(extra) + ' character(s) too long'

        
        