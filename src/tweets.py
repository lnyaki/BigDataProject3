import pandas as pd
import numpy as np
from time import *

'''
In this module, we process tweets, iterate and extract data from them.
'''


def get_tweets_count(userID,tweetsDF):
	'''
	This will count the number of tweets done by a
	'''
	return len(get_tweets_user(userID,tweetsDF))

def get_tweets_user(userID,tweetsDF):
	'''
	This function returns the tweets belonging to a particular userID
	'''
	t0 = time()
	user_id = tweetsDF['user_id'] == userID
	res = tweetsDF[user_id]
	print ("tweet user:", round(time()-t0, 3), "s")
	return res
	#print('In function')
	#usersTweets = []
	#for row in tweetsDF.iterrows():
	#	if int(row['user_id']) == userID:
	#		usersTweets.append(row)
	#return usersTweets

def get_tweets_strings(userID,tweetsDF):
	'''
	Searches for a user's tweets and saves all the text from
	the tweets in 1 string
	'''
	t0 = time()
	#tweetsString = ""
	tweets_user = get_tweets_user(userID,tweetsDF)
	res = tweets_user['text'].str.cat()
	#for tweet in tweets_user.iterrows():
	#	if isinstance(tweet[1]['text'],str):
	#		tweetsString+= tweet[1]['text']
	#print ("tweet strings normal:", round(time()-t0, 3), "s")
	#t1 = time()
	#print(len(tweets_user['text'].str.cat()))
	#print(get_tweets_count(userID,tweetsDF))
	print ("tweet strings optimized:", round(time()-t0, 3), "s")
	return res

def get_all_tweets_data(dataIndexList, tweetsDF):
	'''
	Will extract for all tweets in the tweets dataframe, a list of specified fields.
	'''
	tweetsData = []

	for index, row in tweetsDF.iterrows():
		tweetsData.append(get_single_tweet_data)

	return tweetsData

def get_single_tweet_data(dataIndexList, tweetRow):
	'''
	This function returns the requested data from a single tweet
	
	- dataKeys : a list of index values for the tweetRow, such as 'text', 'retweet_count' or 'user_id'
	- tweetRow : a dataFrame row containing the data of one tweet.
	'''
	tweetData = {}

	for key in dataIndexList:
		tweetData[key] = tweetRow[key]

	return tweetData

