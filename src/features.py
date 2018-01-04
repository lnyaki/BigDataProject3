
###########
# Class A #
###########

# Camisani-Calzolari
HAS_NAME = 'has_name'
HAS_IMAGE = 'has_image'
HAS_ADDRESS = 'has_address'
HAS_BIO = 'has_bio'
HAS_30_FOLLOWERS ='has_30_followers'
BELONGS_TO_A_LIST = 'belongs_to_a_list'
HAS_50_TWEETS = 'has_50_tweets'
URL_IN_PROFILE = 'url_in_profile'
FOLLOWERS_TO_FRIENDS_RATIO_OVER_2 = 'followers_to_friends_ration_over_2'

# State of search
BOT_IN_BIO = 'bot_in_bio'
FRIENDS_TO_FOLLOWERS_RATIO_IS_100 = 'friends_to_followers_ratio_is_100'
DUPLICATE_PROFILE_PICTURE = 'duplicate_profile_picture'

# Socialbakers 
HAS_50_FOLLOWERS 	= 'has_50_followers'
HAS_DEFAULT_IMAGE 	= 'has_default_image'
HAS_NO_BIO 			= 'has_no_bio'
HAS_NO_LOCATION 	= 'has_no_location'
HAS_100_FRIENDS 	= 'has_100_friends'
HAS_NO_TWEETS 		= 'has_no_tweets'

# Stringhini et al.
NUMBER_OF_FRIENDS = 'number_of_friends'
NUMBER_OF_FRIENDS_TWEETS = 'number_of_friends_tweets'
FRIENDS_TO_FOLLOWERS_RATIO = 'friends_to_followers_ratio'

# Yang et al.
AGE = 'age'
FOLLOWING_RATE 		= 'following_rate'

###########
# Class B #
###########

# Camisani-Calzolari
GEOLOCALIZED = 'geolocalized'
IS_FAVORITE = 'is_favorite'
USES_PUNCTUATION = 'uses_punctuation'
USES_HASHTAG = 'uses_hashtag'
USES_IPHONE = 'uses_iphone'
USES_ANDROID = 'uses_android'
USES_FOURSQUARE = 'uses_foursquare'
USES_INSTAGRAM = 'uses_instagram'
USES_TWITTERDOTCOM 'uses_twitterdotcom'
USERID_IN_TWEET = 'userid_in_tweet'
TWEETS_WITH_URL = 'tweets_with_url'
RETWEET_OVER_1 = 'retweet_over_1'
USES_DIFFERENT_CLIENTS = 'uses_different_clients'

#State of Search
DUPLICATE_SENTENCES_ACROSS_ACCOUNTS = 'duplicate_sentences_across_accounts'
API_TWEETS = 'api_tweets'

# Socialbakers
HAS_DUPLICATE_TWEETS 	= 'has_duplicate_tweets'
HIGH_RETWEET_RATIO 		= 'high_retweet_ratio'
HIGH_TWEET_LINK_RATIO	= 'high_tweet_link_ratio'

# Strinhini et al.
TWEET_SIMILARITY 	= 'tweet_similarity'
URL_RATIO 			= 'url_ratio'

# Yang et al.
API_RATIO 			= 'api_ratio'
API_URL_RATIO 		= 'api_url_ratio'
API_TWEET_SIMILARITY 	= 'api_tweet_similarity'



###########
# Class C #
###########

# Yang et al.
BILINK_RATIO = 'bi-link_ratio'
AVERAGE_NEIGHBORS_FOLLOWERS = 'average_neighbors_followers'
AVERAGE_NEIGHBORS_TWEETS 	= 'average_neighbors_tweets'
FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS = 'followings_to_median_neighbors_followers'

def get_camisani_features():
	features = {}

	# class A
	features[HAS_NAME] 							= has_name()
	features[HAS_IMAGE] 						= has_image()
	features[HAS_ADDRESS] 						= has_address()
	features[HAS_BIO] 							= has_bio()
	features[HAS_30_FOLLOWERS] 					= has_30_followers()
	features[BELONGS_TO_A_LIST] 				= belongs_to_a_list()
	features[HAS_50_TWEETS] 					= has_50_tweets()
	features[URL_IN_PROFILE] 					= url_in_profile()
	features[FOLLOWERS_TO_FRIENDS_RATIO_OVER_2] = followers_to_friends_ration_over_2()

	# class B
	features[GEOLOCALIZED] 				= geolocalized()
	features[IS_FAVORITE] 				= is_favorite()
	features[USES_PUNCTUATION] 			= uses_punctuation()
	features[USES_HASHTAG] 				= uses_hashtag()
	features[USES_IPHONE] 				= uses_iphone()
	features[USES_ANDROID] 				= uses_android()
	features[USES_FOURSQUARE] 			= uses_foursquare()
	features[USES_INSTAGRAM] 			= uses_instagram()
	features[USES_TWITTERDOTCOM] 		= uses_twitterdotcom()
	features[USERID_IN_TWEET] 			= userid_in_tweet()
	features[TWEETS_WITH_URL] 			= tweets_with_url()
	features[RETWEET_OVER_1] 			= retweet_over_1()
	features[USES_DIFFERENT_CLIENTS] 	= uses_different_clients()

	return features

def get_state_of_search_features():
	features = {}

	# class A
	features[BOT_IN_BIO] 						= bot_in_bio()
	features[FRIENDS_TO_FOLLOWERS_RATIO_IS_100] = friends_to_followers_ratio_is_100()
	features[DUPLICATE_PROFILE_PICTURE] 		= duplicate_profile_picture()
	
	# class B
	features[DUPLICATE_SENTENCES_ACROSS_ACCOUNTS] 	= duplicate_sentences_across_accounts()
	features[API_TWEETS] 							= api_tweets()


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

def has_name():
	pass

def has_image():
	pass

def has_address():
	pass

def has_bio():
	pass

def has_30_followers():
	pass

def belongs_to_a_list():
	pass

def has_50_tweets():
	pass

def url_in_profile():
	pass

def followers_to_friends_ration_over_2():
	pass

def bot_in_bio():
	pass

def friends_to_followers_ratio_is_100():
	pass

def duplicate_profile_picture():
	pass

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

def geolocalized():
	pass
def is_favorite():
	pass

def uses_punctuation():
	pass

def uses_hashtag():
	pass

def uses_iphone():
	pass

def uses_android():
	pass

def uses_foursquare():
	pass

def uses_instagram():
	pass

def uses_twitterdotcom():
	pass

def userid_in_tweet():
	pass

def tweets_with_url():
	pass

def retweet_over_1():
	pass

def uses_different_clients():
	pass

def duplicate_sentences_across_accounts():
	pass

def api_tweets():
	pass

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
