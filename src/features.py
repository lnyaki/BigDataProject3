
###########
# Class A #
###########

# Camisani-Calzolari
HAS_NAME 			= 'has_name'
HAS_IMAGE 			= 'has_image'
HAS_ADDRESS 		= 'has_address'
HAS_BIO 			= 'has_bio'
HAS_30_FOLLOWERS 	='has_30_followers'
BELONGS_TO_A_LIST 	= 'belongs_to_a_list'
HAS_50_TWEETS 		= 'has_50_tweets'
URL_IN_PROFILE 		= 'url_in_profile'
FOLLOWERS_TO_FRIENDS_RATIO_OVER_2 	= 'followers_to_friends_ration_over_2'

# State of search
BOT_IN_BIO 							= 'bot_in_bio'
FRIENDS_TO_FOLLOWERS_RATIO_IS_100 	= 'friends_to_followers_ratio_is_100'
DUPLICATE_PROFILE_PICTURE 			= 'duplicate_profile_picture'

# Socialbakers 
HAS_50_FOLLOWERS 	= 'has_50_followers'
HAS_DEFAULT_IMAGE 	= 'has_default_image'
HAS_NO_BIO 			= 'has_no_bio'
HAS_NO_LOCATION 	= 'has_no_location'
HAS_100_FRIENDS 	= 'has_100_friends'
HAS_NO_TWEETS 		= 'has_no_tweets'

# Stringhini et al.
NUMBER_OF_FRIENDS 			= 'number_of_friends'
NUMBER_OF_FRIENDS_TWEETS 	= 'number_of_friends_tweets'
FRIENDS_TO_FOLLOWERS_RATIO 	= 'friends_to_followers_ratio'

# Yang et al.
AGE 			= 'age'
FOLLOWING_RATE 	= 'following_rate'

###########
# Class B #
###########

# Camisani-Calzolari
GEOLOCALIZED 			= 'geolocalized'
IS_FAVORITE 			= 'is_favorite'
USES_PUNCTUATION 		= 'uses_punctuation'
USES_HASHTAG 			= 'uses_hashtag'
USES_IPHONE 			= 'uses_iphone'
USES_ANDROID 			= 'uses_android'
USES_FOURSQUARE 		= 'uses_foursquare'
USES_INSTAGRAM 			= 'uses_instagram'
USES_TWITTERDOTCOM 		= 'uses_twitterdotcom'
USERID_IN_TWEET 		= 'userid_in_tweet'
TWEETS_WITH_URL 		= 'tweets_with_url'
RETWEET_OVER_1 			= 'retweet_over_1'
USES_DIFFERENT_CLIENTS 	= 'uses_different_clients'

#State of Search
DUPLICATE_SENTENCES_ACROSS_ACCOUNTS = 'duplicate_sentences_across_accounts'
API_TWEETS 							= 'api_tweets'

# Socialbakers
HAS_DUPLICATE_TWEETS 	= 'has_duplicate_tweets'
HIGH_RETWEET_RATIO 		= 'high_retweet_ratio'
HIGH_TWEET_LINK_RATIO	= 'high_tweet_link_ratio'

# Strinhini et al.
TWEET_SIMILARITY 	= 'tweet_similarity'
URL_RATIO 			= 'url_ratio'

# Yang et al.
API_RATIO 				= 'api_ratio'
API_URL_RATIO 			= 'api_url_ratio'
API_TWEET_SIMILARITY 	= 'api_tweet_similarity'



###########
# Class C #
###########

# Yang et al.
BILINK_RATIO 				= 'bi-link_ratio'
AVERAGE_NEIGHBORS_FOLLOWERS = 'average_neighbors_followers'
AVERAGE_NEIGHBORS_TWEETS 	= 'average_neighbors_tweets'
FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS 	= 'followings_to_median_neighbors_followers'

def get_camisani_features(data):
	features = {}

	# class A
	features[HAS_NAME] 			= has_name(data)
	features[HAS_IMAGE] 		= has_image(data)
	features[HAS_ADDRESS] 		= has_address(data)
	features[HAS_BIO] 			= has_bio(data)
	features[HAS_30_FOLLOWERS] 	= has_30_followers(data)
	features[BELONGS_TO_A_LIST] = belongs_to_a_list(data)
	features[HAS_50_TWEETS] 	= has_50_tweets(data)
	features[URL_IN_PROFILE] 	= url_in_profile(data)
	features[FOLLOWERS_TO_FRIENDS_RATIO_OVER_2] = followers_to_friends_ration_over_2(data)

	# class B
	features[GEOLOCALIZED] 				= geolocalized(data)
	features[IS_FAVORITE] 				= is_favorite(data)
	features[USES_PUNCTUATION] 			= uses_punctuation(data)
	features[USES_HASHTAG] 				= uses_hashtag(data)
	features[USES_IPHONE] 				= uses_iphone(data)
	features[USES_ANDROID] 				= uses_android(data)
	features[USES_FOURSQUARE] 			= uses_foursquare(data)
	features[USES_INSTAGRAM] 			= uses_instagram(data)
	features[USES_TWITTERDOTCOM] 		= uses_twitterdotcom(data)
	features[USERID_IN_TWEET] 			= userid_in_tweet(data)
	features[TWEETS_WITH_URL] 			= tweets_with_url(data)
	features[RETWEET_OVER_1] 			= retweet_over_1(data)
	features[USES_DIFFERENT_CLIENTS] 	= uses_different_clients(data)

	return features

def get_state_of_search_features(data):
	features = {}

	# class A
	features[BOT_IN_BIO] 						= bot_in_bio(data)
	features[FRIENDS_TO_FOLLOWERS_RATIO_IS_100] = friends_to_followers_ratio_is_100(data)
	features[DUPLICATE_PROFILE_PICTURE] 		= duplicate_profile_picture(data)
	
	# class B
	features[DUPLICATE_SENTENCES_ACROSS_ACCOUNTS] 	= duplicate_sentences_across_accounts(data)
	features[API_TWEETS] 							= api_tweets(data)


	return features

def get_socialbakers_features(data):
	'''
	Class A : followers ≥ 50, default image after 2
		months, no bio, no location, friends ≥100, 0 tweets 
	
	Class B : tweets spam phrases, same tweet ≥ 3, retweets ≥ 90%,
		tweet-links ≥ 90%
	'''

	features = {}

	#Class A
	features[HAS_50_FOLLOWERS] 	= has_50_followers(data)
	features[HAS_DEFAULT_IMAGE] = has_default_image(60)
	features[HAS_NO_BIO] 		= has_no_bio(data)
	features[HAS_NO_LOCATION] 	= has_no_location(data)
	features[HAS_100_FRIENDS] 	= has_100_friends(data)
	features[HAS_NO_TWEETS] 	= has_no_tweets(data)

	#Class B
	features[HAS_DUPLICATE_TWEETS] 	= has_duplicate_tweets(3)
	features[HIGH_RETWEET_RATIO] 	= has_retweet_ratio(0.9)
	features[BIG_TWEET_LINK_RATIO] 	= has_tweet_links_ratio(0.9)

	

	return features

def get_stringhini_features(data):
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

def get_yang_features(data):
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

def has_name(data):
	pass

def has_image(data):
	pass

def has_address(data):
	pass

def has_bio(data):
	pass

def has_30_followers(data):
	pass

def belongs_to_a_list(data):
	pass

def has_50_tweets(data):
	pass

def url_in_profile(data):
	pass

def followers_to_friends_ration_over_2(data):
	pass

def bot_in_bio(data):
	pass

def friends_to_followers_ratio_is_100(data):
	pass

def duplicate_profile_picture(data):
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

def geolocalized(data):
	pass
def is_favorite(data):
	pass

def uses_punctuation(data):
	pass

def uses_hashtag(data):
	pass

def uses_iphone(data):
	pass

def uses_android(data):
	pass

def uses_foursquare(data):
	pass

def uses_instagram(data):
	pass

def uses_twitterdotcom(data):
	pass

def userid_in_tweet(data):
	pass

def tweets_with_url(data):
	pass

def retweet_over_1(data):
	pass

def uses_different_clients(data):
	pass

def duplicate_sentences_across_accounts(data):
	pass

def api_tweets(data):
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
