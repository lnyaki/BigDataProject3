user_tweets = tweetsDF['user_id']== userID
def get_tweets_with_url_ratio(userID, tweetsDF):
	t0 = time()
	user_tweets = tweetsDF['user_id'] == userID
	#urlTweets 	= tweetsDF[user_tweets &(tweetsDF['text'].apply(lambda tweet: tweet_contains_url(tweet)))]
	urlTweets 	= tweetsDF[user_tweets & tweetsDF['text']]
	new_value = urlTweets['text'].apply(lambda tweet: tweet_contains_url(tweet))
	#print(new_value)
	#print("TEST:", round(time()-t0, 3), "s")
	tweets_with_url 	= new_value.mean()
	#print("tweets_with_url: "+str(tweets_with_url))

	user_tweets_count 	= count_user_tweets(userID,tweetsDF)
	if(user_tweets_count == 0):
		user_tweets_count = 0.001
		
	return float(tweets_with_url)/float(user_tweets_count)


def tweet_contains_url(tweet):
	return has_url(tweet)

def get_api_tweets_count(userTweetsDF):
	'''
	The tweetDF only contains tweets from a single user
	'''
	tweets = userTweetsDF[userTweetsDF['text'].apply(lambda tweet : tweet.count("API")>0)]

	return len(tweets.tolist())

def retweet_ratio(userID, tweetsDF):
	tweets = tweetsDF[tweetsDF['user_id'] == userID]

	tweetsCount = tweets.shape[0]

	retweets = tweets[tweets['retweet_count']>0].shape[0]

	if(tweetsCount == 0):
		print("-----------------Retweet 0")
		return 0

	else:
		res = retweets/tweetsCount
		print("-----------------Retweet : "+str(res))
		return res