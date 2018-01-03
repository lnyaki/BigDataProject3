

#Class A
NUMBER_OF_FRIENDS = 'number_of_friends'
NUMBER_OF_FRIENDS_TWEETS = 'number_of_friends_tweets'
FRIENDS_TO_FOLLOWERS_RATIO = 'friends_to_followers_ratio'
AGE = 'age'
FOLLOWING_RATE 		= 'following_rate'
HAS_50_FOLLOWERS 	= 'has_50_followers'
HAS_DEFAULT_IMAGE 	= 'has_default_image'
HAS_NO_BIO 			= 'has_no_bio'
HAS_NO_LOCATION 	= 'has_no_location'
HAS_100_FRIENDS 	= 'has_100_friends'
HAS_NO_TWEETS 		= 'has_no_tweets'


# Class B
TWEET_SIMILARITY 	= 'tweet_similarity'
URL_RATIO 			= 'url_ratio'
API_RATIO 			= 'api_ratio'
API_URL_RATIO 		= 'api_url_ratio'
API_TWEET_SIMILARITY 	= 'api_tweet_similarity'
HAS_DUPLICATE_TWEETS 	= 'has_duplicate_tweets'
HIGH_RETWEET_RATIO 		= 'high_retweet_ratio'
HIGH_TWEET_LINK_RATIO	= 'high_tweet_link_ratio'


# Class C
BILINK_RATIO = 'bi-link_ratio'
AVERAGE_NEIGHBORS_FOLLOWERS = 'average_neighbors_followers'
AVERAGE_NEIGHBORS_TWEETS 	= 'average_neighbors_tweets'
FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS = 'followings_to_median_neighbors_followers'

def get_camisani_features():
	features = {}

	return features

def get_state_of_search_features():
	features = {}

	return features

def get_socialbakers_features():
	'''
	Class A : followers ≥ 50, default image after 2
		months, no bio, no location, friends ≥100, 0 tweets 
	
	Class B : tweets spam phrases, same tweet ≥ 3, retweets ≥ 90%,
		tweet-links ≥ 90%
	'''

	features = {}

	#Class A
	features[HAS_50_FOLLOWERS] 	= has_50_followers()
	features[HAS_DEFAULT_IMAGE] = has_default_image(60)
	features[HAS_NO_BIO] 		= has_no_bio()
	features[HAS_NO_LOCATION] 	= has_no_location()
	features[HAS_100_FRIENDS] 	= has_100_friends()
	features[HAS_NO_TWEETS] 	= has_no_tweets()

	#Class B
	features[HAS_DUPLICATE_TWEETS] 	= has_duplicate_tweets(3)
	features[HIGH_RETWEET_RATIO] 	= has_retweet_ratio(0.9)
	features[BIG_TWEET_LINK_RATIO] 	= has_tweet_links_ratio(0.9)

	

	return features

def get_stringhini_features():
	'''
	Class A : number of friends, number of friends tweets, friends/(followersˆ2)

	Class B : tweet similarity, URL ratio
	'''
	features = {}

	# Class A
	features[NUMBER_OF_FRIENDS] 			= get_friends_count(data)
	features[NUMBER_OF_FRIENDS_TWEETS] 		= get_friends_tweet_count(data)
	features[FRIENDS_TO_FOLLOWERS_RATIO] 	= get_friends_to_followers_ratio(data)

	# Class B
	features[TWEET_SIMILARITY] 	= get_tweet_similarity(data)
	features[URL_RATIO] 		= get_url_ratio(data)

	return features

def get_yang_features():
	'''
	class A : age, following rate

	Class B : API ratio, API URL ratio, API tweet similarity

	Class C: bi-link ratio, average
		neighbors’ followers, average
		neighbors’ tweets, followings
		to median neighbor’s followers
	'''
	features = {}

	# Class A features
	features[AGE] 				= get_age(data)
	features[FOLLOWING_RATE] 	= get_following_rate(data)

	# Class B features
	features[API_RATIO] 			= get_api_ratio(data)
	features[API_URL_RATIO] 		= get_api_url_ratio(data)
	features[API_TWEET_SIMILARITY] 	= get_api_tweet_similarity(data)

	# Class C features
	features[BILINK_RATIO] 					= get_bilink_ratio(data)
	features[AVERAGE_NEIGHBORS_FOLLOWERS] 	= get_average_neighbors_followers(data)
	features[AVERAGE_NEIGHBORS_TWEETS] 		= get_average_neighbors_tweets(data)
	features[FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS] = get_followings_to_median(data)

	return features

'''
TODO: create functions that retrieve each individual feature, below
'''

# Class A features
def get_age(data):
	pass

def get_following_rate(data):
	pass

def get_friends_count(data):
	pass

def get_friends_tweet_count(data):
	pass

def get_friends_to_followers_ratio(data):
	pass

def has_50_followers(data):
	pass

def has_default_image(data):
	pass

def has_no_bio(data):
	pass

def has_no_location(data):
	pass

def has_100_friends(data):
	pass

def has_no_tweets(data):
	pass


# Class B features
def get_api_ratio(data):
	pass

def get_api_url_ratio(data):
	pass

def get_api_tweet_similarity(data):
	pass

def get_tweet_similarity(data):
	pass

def get_url_ratio(data):
	pass

def has_duplicate_tweets(data,duplicate_count):
	pass

def has_retweet_ratio(data, ratio):
	pass

def has_tweet_links_ratio(data, ratio):
	pass


# Class C featrues
def get_bilink_ratio(data):
	pass

def get_average_neighbors_followers(data):
	pass

def get_average_neighbors_tweets(data):
	pass

def get_followings_to_median(data):
	pass
