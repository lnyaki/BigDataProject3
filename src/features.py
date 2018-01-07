import pandas as pd
import sys
import url_finder
from datetime import datetime
from dateutil.parser import parse
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
ACCOUNT_AGE		= 'account_age'
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

#*********************************
#      Features set names        *
#*********************************
CAMISANI 		= 'camisani'		#'Camisani-Calzolari'
STATEOFSEARCH	= 'stateofsearch'	#'State of search'
SOCIALBAKERS 	= 'socialbakers'	#'SocialBakers'
STRINGHINI 		= 'stringhini'		#'Stringhini et al'
YANG 			= 'yang' 			#'Yang et al'

def get_features(featureSetName, dataframes):
	features = {}

	if(featureSetName == CAMISANI):
		features = get_camisani_features(dataframes)

	elif(featureSetName == STATEOFSEARCH):
		features = get_state_of_search_features(dataframes)

	elif(featureSetName == SOCIALBAKERS):
		features = get_socialbakers_features(dataframes)

	elif(featureSetName == STRINGHINI):
		features = get_stringhini_features(dataframes)

	elif(featureSetName == YANG):
		features = get_yang_features(dataframes)
	else:
		print("Error Unknown feature set specified : "+featureSetName)

	return features


def get_camisani_features(dataframes):
	camisaniFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		camisaniFeatures.append(get_single_user_state_of_search_features(row,usersDF,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return camisaniFeatures

def get_single_user_camisani_features(userRow, userDF, tweetsDF):
	'''
	Class A : has name, has image, has address, has bio, followers >= 30, belongs to a list, 
	tweets >= 50, URL in profile, 2xfollowers >= friends

	Class B : geo, is favorite, uses punctuation, uses #, uses iphone, uses android, uses foursquare,
	uses twitter.com, userId in tweet, retweet >= 1, uses different clients
	'''
	features = {}

	# class A
	features[HAS_NAME] 			= has_name(userRow)
	features[HAS_IMAGE] 		= has_image(userRow)
	features[HAS_ADDRESS] 		= has_address(userRow)
	features[HAS_BIO] 			= has_bio(userRow)
	features[HAS_30_FOLLOWERS] 	= has_30_followers(userRow)
	features[BELONGS_TO_A_LIST] = belongs_to_a_list(userRow)
	features[HAS_50_TWEETS] 	= has_50_tweets(userRow)
	features[URL_IN_PROFILE] 	= url_in_profile(userRow)
	features[FOLLOWERS_TO_FRIENDS_RATIO_OVER_2] = followers_to_friends_ration_over_2(userRow)

	# class B
	features[GEOLOCALIZED] 				= geolocalized(userRow)
	features[IS_FAVORITE] 				= is_favorite(userRow)
	features[USES_PUNCTUATION] 			= uses_punctuation(userRow)
	features[USES_HASHTAG] 				= uses_hashtag(userRow)
	features[USES_IPHONE] 				= uses_iphone(userRow)
	features[USES_ANDROID] 				= uses_android(userRow)
	features[USES_FOURSQUARE] 			= uses_foursquare(userRow)
	features[USES_INSTAGRAM] 			= uses_instagram(userRow)
	features[USES_TWITTERDOTCOM] 		= uses_twitterdotcom(userRow)
	features[USERID_IN_TWEET] 			= userid_in_tweet(userRow)
	features[TWEETS_WITH_URL] 			= tweets_with_url(userRow)
	features[RETWEET_OVER_1] 			= retweet_over_1(userRow)
	features[USES_DIFFERENT_CLIENTS] 	= uses_different_clients(userRow)

	return features

def get_state_of_search_features(dataframes):
	stateofsearchFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		stateofsearchFeatures.appen(get_single_user_state_of_search_features(row,usersDF,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return stateofsearchFeatures


def get_single_user_state_of_search_features(userRow, userDF, tweetsDF):
	'''
	Class A : bot in biography, friends/followers > 100, duplicate profile pictures

	Class B : same sentence to many accounts, tweet from API
	'''

	features = {}

	# class A
	features[BOT_IN_BIO] 						= bot_in_bio(userRow)
	features[FRIENDS_TO_FOLLOWERS_RATIO_IS_100] = friends_to_followers_ratio_is_100(userRow)
	features[DUPLICATE_PROFILE_PICTURE] 		= duplicate_profile_picture(userRow)
	
	# class B
	features[DUPLICATE_SENTENCES_ACROSS_ACCOUNTS] 	= duplicate_sentences_across_accounts(userRow)
	features[API_TWEETS] 							= api_tweets(userRow)


	return features

def get_socialbakers_features(dataframes):
	socialbakersFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		socialbakersFeatures.append(get_single_user_socialbakers_features(row,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return socialbakersFeatures

def get_single_user_socialbakers_features(userRow, tweetsDF):
	'''
	Class A : followers ≥ 50, default image after 2
		months, no bio, no location, friends ≥100, 0 tweets 
	
	Class B : tweets spam phrases, same tweet ≥ 3, retweets ≥ 90%,
		tweet-links ≥ 90%
	'''

	features = {}

	#Class A

	#TODO : ce n'est pas 50 followers, c'est un ratio de 50:1 entre friends et followers
	features[HAS_50_FOLLOWERS] 	= has_50_followers(userRow)
	features[HAS_DEFAULT_IMAGE] = has_default_image(userRow)
	features[HAS_NO_BIO] 		= has_no_bio(userRow)
	features[HAS_NO_LOCATION] 	= has_no_location(userRow)
	features[HAS_100_FRIENDS] 	= has_100_friends(userRow)
	features[HAS_NO_TWEETS] 	= has_no_tweets(userRow)

	#Class B
	features[HAS_DUPLICATE_TWEETS] 	= has_duplicate_tweets(userRow,tweetsDF,3)
	features[HIGH_RETWEET_RATIO] 	= has_retweet_ratio(userRow,tweetsDF,0.9)
	features[HIGH_TWEET_LINK_RATIO] = has_tweet_links_ratio(userRow, tweetsDF,0.9)

	return features

def get_stringhini_features(dataframes):
	'''

	'''
	stringhiniFeatures = []

	usersDF 	= dataframes['users']
	friendsDF 	= dataframes['friends']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		stringhiniFeatures.append(get_single_user_stringhini_features(row,usersDF, friendsDF,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return stringhiniFeatures

def get_single_user_stringhini_features(userRow, usersDF,friendsDF, tweetsDF):
	'''
	Class A : number of friends, number of friends tweets, friends/(followersˆ2)

	Class B : tweet similarity, URL ratio
	'''
	features = {}

	# Class A
	features[NUMBER_OF_FRIENDS] 			= get_friends_count(userRow)
	features[NUMBER_OF_FRIENDS_TWEETS] 		= get_friends_tweet_count(userRow,friendsDF,usersDF)
	features[FRIENDS_TO_FOLLOWERS_RATIO] 	= get_stringhini_friends_to_followers_ratio(userRow)

	# Class B
	features[TWEET_SIMILARITY] 	= get_tweet_similarity(userRow,tweetsDF)
	features[URL_RATIO] 		= get_url_ratio(userRow, tweetsDF)

	return features

def get_yang_features(dataframes):
	yangFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		yangFeatures.append(get_single_user_yang_features(row, tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return yangFeatures


def get_single_user_yang_features(userRow, tweetsDF):
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
	features[ACCOUNT_AGE] 		= get_account_age(userRow)
	features[FOLLOWING_RATE] 	= get_following_rate(userRow)

	# Class B features
	features[API_RATIO] 			= get_api_ratio(userRow)
	features[API_URL_RATIO] 		= get_api_url_ratio(userRow)
	features[API_TWEET_SIMILARITY] 	= get_api_tweet_similarity(userRow)

	# Class C features
	features[BILINK_RATIO] 					= get_bilink_ratio(userRow)
	features[AVERAGE_NEIGHBORS_FOLLOWERS] 	= get_average_neighbors_followers(userRow)
	features[AVERAGE_NEIGHBORS_TWEETS] 		= get_average_neighbors_tweets(userRow)
	features[FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS] = get_followings_to_median(userRow)

	return features

def get_dataframes(datasetDirectory, featureSetName):
	'''
	- BaseFilesDirectory is the base directory of the dataset we are using :
		E13,FAK,FSF,HUM,INT,TFP,TWT.
	- featureSetName is the name of the feature set for which we want to load the dataframes.

	The function returns the proper required dataframes for the featureSetName specified.
	'''
	fileNames = {}
	dataframes = {}

	if(featureSetName == CAMISANI):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv'}

	elif(featureSetName == STATEOFSEARCH):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv'}

	elif(featureSetName == SOCIALBAKERS):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv'}

	elif(featureSetName == STRINGHINI):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv','friends' : 'friends.csv'}

	elif(featureSetName == YANG):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv'}

	# We load the dataframes from the files specified above, in a dataframe dictionary
	for key, filename in fileNames.items():
		totalPath = datasetDirectory + '/'+ filename

		print("Loading "+ totalPath)

		try:
			dataframes[key] = pd.read_csv(totalPath, encoding='latin-1')

		except Exception as e:
			print("Error while reading file "+totalPath)
			print(e)

		print(dataframes[key].head(5))

	return dataframes 

'''
TODO: create functions that retrieve each individual feature, below
'''

# Class A features

def has_name(userRow):
	return False

def has_image(userRow):
	return False

def has_address(userRow):
	return False

def has_bio(userRow):
	return False

def has_30_followers(userRow):
	return  int(userRow['followers_count']) >= 30

def belongs_to_a_list(userRow):
	return False

def get_tweets_count(userRow):
	return int(userRow[''])

def has_50_tweets(userRow):
	return False

def url_in_profile(userRow):
	return False

def followers_to_friends_ration_over_2(userRow):
	return False

def bot_in_bio(userRow):
	return False

def friends_to_followers_ratio_is_100(userRow):
	threshold = 100

	return get_friends_to_followers_ratio(userRow) >= threshold

def duplicate_profile_picture(userRow):
	return False

def get_account_age(userRow):
	# Date format : Thu Apr 06 15:24:15 +0000 2017
	account_creation = datetime.strptime(userRow['created_at'],'%a %b %d %H:%M:%S %z %Y')
	#Two lines below, to prevent error : can't subtract offset-naive and offset-aware datetimes
	# Solution from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
	timezone = account_creation.tzinfo
	today = datetime.now(timezone)

	return (today - account_creation).days

def get_following_rate(userRow):
	return 0

def get_friends_count(userRow):
	return int(userRow['friends_count'])

def get_friends_tweet_count(userRow,friendsDF,usersDF):
	return 0

def get_friends_to_followers_ratio(userRow):
	return int(userRow['friends_count'])/int(userRow['followers_count'])

def get_stringhini_friends_to_followers_ratio(userRow):
	followers = int(userRow['followers_count'])

	return int(userRow['friends_count'])/(followers*followers)

def has_50_followers(userRow):
	return False

def has_default_image(userRow):
	return False

def has_no_bio(userRow):
	return False

def has_no_location(userRow):
	return False

def has_100_friends(userRow):
	return False

def has_no_tweets(userRow):
	return False


# Class B features

def geolocalized(userRow):
	return False

def is_favorite(userRow):
	return False

def uses_punctuation(userRow):
	return False

def uses_hashtag(userRow):
	return False

def uses_iphone(userRow):
	return False

def uses_android(userRow):
	return False

def uses_foursquare(userRow):
	return False

def uses_instagram(userRow):
	return False

def uses_twitterdotcom(userRow):
	return False

def userid_in_tweet(userRow):
	return False

def tweets_with_url(tweetsDF):
	return 0

def retweet_over_1(userRow):
	return False

def uses_different_clients(userRow):
	return False

def duplicate_sentences_across_accounts(userRow):
	return False

def api_tweets(userRow):
	return 0

def get_api_ratio(userRow):
	# tweets sent from api over total number of tweets
	return 0

def get_api_url_ratio(userRow):
	return 0

def get_api_tweet_similarity(userRow):
	return 0

def get_tweet_similarity(userRow,tweetsDF):
	return 0

def get_url_ratio(userRow, tweetsDF):
	'''ratio of tweets with a url'''
	return 0

def has_duplicate_tweets(userRow, tweetsDF,duplicate_threshold):
	return False

def has_retweet_ratio(userRow,tweetsDF, ratio_threshold):
	'''
	Returns true if the ratio calculated is superior or equal to the ratio_threshold.
	Returns false otherwise.
	'''
	return False

def has_tweet_links_ratio(userRow, tweetsDF, ratio_threshold):
	'''
	Returns true if the ratio calculated is superior or equal to the ratio_threshold.
	Returns false otherwise.
	'''
	return False


# Class C featrues
def get_bilink_ratio(userRow):
	#Bi-directional link is when two account follow each other
	return 0

def get_average_neighbors_followers(userRow):
	#Average the number of followers of the friends of the user.
	return 0

def get_average_neighbors_tweets(userRow):
	#Average the number of tweets of the friends of the user.
	return 0

def get_followings_to_median(userRow):
	'''
	Ratio between number of friends and the median of the followers of its friends.
	'''
	return 0

'''
To use (prototype) go to root directory:
	command example : python3 src/features.py "data/E13" yang
'''
if(__name__ == "__main__"):
	directory = sys.argv[1]

	featureSetName = sys.argv[2]
	dataframes = get_dataframes(directory,featureSetName)

	print("OK, ca passe")
	features 	= pd.DataFrame(get_features(featureSetName, dataframes))

	print("Features : ")
	print(features)