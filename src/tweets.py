import url_finder
'''
In this module, we process tweets, iterate and extract data from them.
'''
def has_tweets(userID,tweetsDF):
	exit = False
	has_tweets = False
	l = len(tweetsDF)
	i = 0

	while not exit:
		tweet = tweetsDF.loc(i)

		if(tweet['user_id'] == userID):
			exit = True
			has_tweets = True

		else:
			i = i+1

			if(i>=l):
				exit = True

	return has_tweets

def get_tweets_count(userID,tweetsDF):
	'''
	This will count the number of tweets done by a
	'''
	#return len(get_tweets_user(userID,tweetsDF))
	return tweetsDF[tweetsDF['user_id'] == userID].count()

def get_tweets_user(userID,tweetsDF):
	'''
	This function returns the tweets belonging to a particular userID
	'''
	'''
	usersTweets = []
	for index,row in tweetsDF.iterrows():
		if int(row['user_id']) == userID:
			usersTweets.append(row)
	return usersTweets
	'''
	return tweetsDF[tweetsDF['user_id']== userID]

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

def get_tweets_with_url_ratio(userID, tweetsDF):
	user_tweets_count = 0
	tweets_with_url = 0

	for index, row in tweetsDF.iterrows():
		if(row['user_id'] == userID):
			user_tweets_count = user_tweets_count+1

			if(tweet_contains_url(row['text'])):
				tweets_with_url = tweets_with_url+1

	return tweets_with_url/user_tweets_count

def tweet_contains_url(tweet):
	return url_finder.has_url(tweet)