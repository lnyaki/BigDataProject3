'''
In this module, we process tweets, iterate and extract data from them.
'''


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

