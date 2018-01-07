'''
In this module, we process tweets, iterate and extract data from them.
'''


def get_tweets_count(userID,tweetsDF):
	'''
	This will count the number of tweets done by a
	'''
	return len(get_tweets_user(user_id,tweetsDF))

def get_tweets_user(userID,tweetsDF):
	'''
	This function returns the tweets belonging to a particular userID
	'''
	usersTweets = []
	for index,row in tweetsDF.iterrows():
		if int(row['user_id']) == userID:
			usersTweets.append(row)
	return usersTweets

def get_tweets_strings(userID,tweetsDF):
	'''
	Searches for a user's tweets and saves all the text from
	the tweets in 1 string
	'''
	tweetsString = ""
	for tweet in get_tweets_user(userID,tweetsDF):
		tweetsString+= tweet['text']
	return tweetsString

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

