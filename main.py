from twitter import *
import json

token = '14078916-JWk5ow8bIS9Qoeqd5TT4CTl5z0PdeUKPLAGN9OLqb'
token_secret = '1SlOhIHjRNKMLmUEqjxA5DAcKhIr5Y10jIpw5S8L1Ljsv'
consumer_key = 'uBcwNK6ErEAXenrBZMDEthib2'
consumer_secret = 'SbP0tOW8PxfVLloGlNuSC0CGhKbdNFdCjXsIBoDQgnz593bAoB'

def print_hi():
    t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    results = t.search.tweets(q="#crypto")
    print(results)

if __name__ == '__main__':
    print_hi()

