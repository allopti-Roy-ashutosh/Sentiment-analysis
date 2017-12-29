import tweepy
from twython import Twython
#import csv
#import pandas as pd
import simplejson as json
import io

fw=io.open("twitter.json",'w',encoding='utf8')
 
def process_or_store(tweet):
    print json.dumps(tweet) 

####input your credentials here
consumer_key = 'iMQHwNSMLTgnNpPztjacyQ492'
consumer_secret = 'lprQgyyavnTMTzNPPj0GbWaWdl9UcszVg5ST9v34WE51fsoimk'
access_token = '457433538-JWUETk7ZBuNfNcm41m2aGaDVtHj0mZZpRM38pzYK'
access_token_secret = 'sTyXZcvBqSaXcQY73I2sJzvsNIwGTT5gZE3lKrS1G9e0T'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


user = api.me()

'''print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))'''

for friend in tweepy.Cursor(api.friends).items():                   #to get the list of followers
        fw.write(friend.name+"\n")
        process_or_store(friend._json)



"""import tweepy,time,sys
from tweepy import OAuthHandler
import json
import io
fw=io.open("twitter.txt",'w',encoding='utf8')
 
def process_or_store(tweet):
    print json.dumps(tweet)                                                 #use tweet['text'] to print only the text part
 
def read_tweets():
    
    
 
    for status in tweepy.Cursor(api.home_timeline).items(10):   #to read tweets from timeline
        fw.write(status.text+"\n")
        process_or_store(status._json)
 
 
    for friend in tweepy.Cursor(api.friends).items():                   #to get the list of followers
        fw.write(friend.name+"\n")
        process_or_store(friend._json)
 
    for tweet in tweepy.Cursor(api.user_timeline).items(10):          #to get our tweets
        process_or_store(tweet._json)"""
 
fw.close()
