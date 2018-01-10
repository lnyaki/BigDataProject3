from url_finder import *
import pandas as pd
import numpy as np
from time import *
'''
In this module, we process tweets, iterate and extract data from them.
'''
def has_tweets(userID,tweetsDF):
	return tweetsDF[tweetsDF['user_id'] == userID].empty

def get_tweets_count(userID,tweetsDF):
	'''
	This will count the number of tweets done by a
	'''
	userTweets = get_tweets_user(userID,tweetsDF)

	return len(userTweets)

def get_tweets_user(userID,tweetsDF):
	'''
	This function returns the list of tweets belonging to a particular userID
	'''
	return tweetsDF['text'][tweetsDF['user_id']== userID].tolist()

def get_tweets_dataframe_user(userID,tweetsDF):
	'''
	This function returns the tweets belonging to a particular userID
	'''
	#t0 = time()
	user_id = tweetsDF['user_id'] == userID
	res = tweetsDF[user_id]
	#print ("tweet user:", round(time()-t0, 3), "s")
	return res

def count_user_tweets(userID, tweetsDF):
	return len(get_tweets_user(userID,tweetsDF))


def get_avg_friends_tweets(friendsIDlist,tweetsDF):
	friends_count 		= len(friendsIDlist)
	total_tweet_count 	= 0

	for friendID in friendsIDlist:
		total_tweet_count = total_tweet_count + count_user_tweets(friendID, tweetsDF)

	return total_tweet_count/friends_count



def get_tweets_strings(userID,tweetsDF):
	'''
	Searches for a user's tweets and saves all the text from
	the tweets in 1 string
	'''
	#t0 = time()
	#tweetsString = ""
	tweets_user = get_tweets_dataframe_user(userID,tweetsDF)
	res = tweets_user['text'].str.cat()
	#for tweet in tweets_user.iterrows():
	#	if isinstance(tweet[1]['text'],str):
	#		tweetsString+= tweet[1]['text']
	#print ("tweet strings normal:", round(time()-t0, 3), "s")
	#t1 = time()
	#print(len(tweets_user['text'].str.cat()))
	#print(get_tweets_count(userID,tweetsDF))
	#print ("tweet strings optimized:", round(time()-t0, 3), "s")
	return res


def get_tweets_with_url_ratio(userID, tweetsDF):
	user_tweets = tweetsDF['user_id']== userID
	
	urlTweets 	= tweetsDF['user_id'][user_tweets &(tweetsDF['text'].apply(lambda tweet: tweet_contains_url(tweet)))]
	urlTweets = urlTweets.tolist()

	tweets_with_url 	= len(urlTweets)
	user_tweets_count 	= count_user_tweets(userID,tweetsDF)


	return tweets_with_url/user_tweets_count


def tweet_contains_url(tweet):
	return url_finder.has_url(tweet)