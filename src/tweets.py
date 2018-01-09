import url_finder
import pandas as pd
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


def count_user_tweets(userID, tweetsDF):
	return len(get_tweets_user(userID,tweetsDF))


def get_avg_friends_tweets(friends,tweetsDF):
	pass


def get_tweets_strings(userID,tweetsDF):
	'''
	Searches for a user's tweets and saves all the text from
	the tweets in 1 string
	'''
	tweetsString = ""
	for tweet in get_tweets_user(userID,tweetsDF):
		tweetsString+= tweet['text']
	return tweetsString


def get_tweets_with_url_ratio(userID, tweetsDF):
	user_tweets = tweetsDF['user_id']== userID
	
	urlTweets 	= tweetsDF['user_id'][user_tweets &(tweetsDF['text'].apply(lambda tweet: tweet_contains_url(tweet)))]
	urlTweets = urlTweets.tolist()

	tweets_with_url 	= len(urlTweets)
	user_tweets_count 	= count_user_tweets(userID,tweetsDF)


	return tweets_with_url/user_tweets_count


def tweet_contains_url(tweet):
	return url_finder.has_url(tweet)