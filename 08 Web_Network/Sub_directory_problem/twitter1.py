import urllib.request, urllib.parse, urllib.error
from twitterAPI import twurl      #this will break the code
# import twurl
# import ssl

# PY4E book, typed page 176
# Goal: retrieves the timeline for a Twitter user, returns it in JSON format in a string, print first 250 chars of the string
    
# Twitter web service are accessed using a URL like this: 
    # but you have to construct the full url with params
TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
# the full url will look like e.g.
# https://api.twitter.com/1.1/statuses/user_timeline.json?count=2&oauth_version=1.0&oauth_token=101...SGI&screen_name=drchuck&oauth_nonce=09239679&oauth_timestamp=1380395644&oauth_signature=rLK...BoD&oauth_consumer_key=h7Lu...GNg&oauth_signature_method=HMAC-SHA

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url, '\n')
    
    
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    print(data[:250], '\n')       # print first 250 chars of the string
    # unlike Socket, urlopen autostrips headers, so you v to get it. 
    headers = dict(connection.getheaders())
    # printing headers
    print('Remaining', headers['x-rate-limit-remaining'])