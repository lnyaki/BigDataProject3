import pandas as pd
import sys
from datetime import datetime
from dateutil.parser import parse
import itertools
import string
from tweets import *
from url_finder import *
from users import *
import math
from time import *
from difflib import SequenceMatcher
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
NUMBER_OF_TWEETS_SENT		= 'number_of_tweets_sent'
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
DUPLICATE_SENTENCES_ACROSS_TWEETS = 'duplicate_sentences_across_tweets'
API_TWEETS 							= 'api_tweets'

# Socialbakers
HAS_DUPLICATE_TWEETS 	= 'has_duplicate_tweets'
HIGH_RETWEET_RATIO 		= 'high_retweet_ratio'
HIGH_TWEET_LINK_RATIO	= 'high_tweet_link_ratio'


# Strinhini et al.
TWEET_SIMILARITY 	= 'tweet_similarity'
URL_RATIO 			= 'url_ratio'
UNIQUE_FRIENDS_NAME_RATIO = 'unique_friends_name'

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
CLASS_A 		= 'A'
CLASS_C 		= 'C'

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

	elif(featureSetName == CLASS_A):
		features = get_class_A_features(dataframes)

	elif(featureSetName == CLASS_C):
		features = get_class_C_features(dataframes)

	else:
		print("Error Unknown feature set specified : "+featureSetName)

	return features

def get_class_A_features(dataframes):
	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	features 	= []

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():

		features.append(get_single_class_A_features(row,usersDF, tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return features


def get_single_class_A_features(userRow, usersDF,tweetsDF):
	#Class A features = profile-based features
	userID = userRow['id']

	#Camisani class A
	features = {}
	features[HAS_NAME] 			= has_name(userRow)
	features[HAS_IMAGE] 		= has_image(userRow)
	features[HAS_ADDRESS] 		= has_address(userRow)
	features[HAS_BIO] 			= has_bio(userRow)
	features[HAS_30_FOLLOWERS] 	= has_30_followers(userRow)
	features[BELONGS_TO_A_LIST] = belongs_to_a_list(userRow)
	features[HAS_50_TWEETS] 	= has_50_tweets(userRow)
	features[URL_IN_PROFILE] 	= url_in_profile(userRow)
	features[FOLLOWERS_TO_FRIENDS_RATIO_OVER_2] = followers_to_friends_ration_over_2(userRow)

	#State of search class A
	features[BOT_IN_BIO] 						= bot_in_bio(userRow)
	features[FRIENDS_TO_FOLLOWERS_RATIO_IS_100] = friends_to_followers_ratio_is_100(userRow)
	features[DUPLICATE_PROFILE_PICTURE] 		= duplicate_profile_picture(userRow,usersDF)

	#Social bakers class A
	features[HAS_50_FOLLOWERS] 	= has_50_followers(userRow)
	features[HAS_DEFAULT_IMAGE] = has_default_image(userRow)
	#features[HAS_NO_BIO] 		= has_no_bio(userRow) #Same as has_bio from camisani
	features[HAS_NO_LOCATION] 	= has_no_location(userRow)
	features[HAS_100_FRIENDS] 	= has_100_friends(userRow)
	features[HAS_NO_TWEETS] 	= has_no_tweets(userID, tweetsDF)
	
	#Stringhini class A
	features[NUMBER_OF_FRIENDS] 			= get_friends_count(userRow)
	features[FRIENDS_TO_FOLLOWERS_RATIO] 	= get_stringhini_friends_to_followers_ratio(userRow)

	#Yang class A
	features[ACCOUNT_AGE] 		= get_account_age(userRow)

	return features 

def get_class_C_features(dataframes):
	#Class C features = all features

	features = get_class_A_features(dataframes)

	#Camisani Class B
	features[GEOLOCALIZED] 				= geolocalized(userRow,tweetsDF)
	features[IS_FAVORITE] 				= is_favorite(userRow,tweetsDF)
	features[USES_PUNCTUATION] 			= uses_punctuation(userRow,tweetsDF)
	features[USES_HASHTAG] 				= uses_hashtag(userRow,tweetsDF)
	features[USES_IPHONE] 				= uses_iphone(userRow,tweetsDF)
	features[USES_ANDROID] 				= uses_android(userRow,tweetsDF)
	features[USES_FOURSQUARE] 			= uses_foursquare(userRow,tweetsDF)
	features[USES_INSTAGRAM] 			= uses_instagram(userRow,tweetsDF)
	features[USES_TWITTERDOTCOM] 		= uses_twitterdotcom(userRow,tweetsDF)
	features[USERID_IN_TWEET] 			= userid_in_tweet(userRow,tweetsDF)
	features[TWEETS_WITH_URL] 			= tweets_with_url(userRow,tweetsDF)
	features[RETWEET_OVER_1] 			= retweet_over_1(userRow,tweetsDF)
	features[USES_DIFFERENT_CLIENTS] 	= uses_different_clients(userRow,tweetsDF)

	#State of search Class B
	features[DUPLICATE_SENTENCES_ACROSS_ACCOUNTS] 	= duplicate_sentences_across_accounts(userRow,tweetsDF)
	features[API_TWEETS] 							= api_tweets(userRow,tweetsDF)

	#Social Bakers class B
	features[HAS_DUPLICATE_TWEETS] 	= has_duplicate_tweets(userRow,tweetsDF,3)
	features[HIGH_RETWEET_RATIO] 	= has_retweet_ratio(userRow,tweetsDF,0.9)
	features[HIGH_TWEET_LINK_RATIO] = has_tweet_links_ratio(userRow, tweetsDF,0.9)

	#Stringhini class B
	features[NUMBER_OF_TWEETS_SENT]		= get_tweets_count(userID,tweetsDF)
	#features[TWEET_SIMILARITY] 		= get_tweet_similarity(userRow,tweetsDF)	#comment calculer?
	features[URL_RATIO] 				= get_url_ratio(userRow, tweetsDF)
	features[UNIQUE_FRIENDS_NAME_RATIO] = get_unique_friends_name_ratio(userID,usersDF,friendsDF)
	
	#Yang class B (Comment calculer API?)
	#features[API_RATIO] 				= get_api_ratio(userRow)
	#features[API_URL_RATIO] 			= get_api_url_ratio(userRow)
	#features[API_TWEET_SIMILARITY] 	= get_api_tweet_similarity(userRow)

	#Yang class C
	#features[BILINK_RATIO] 				= get_bilink_ratio(userRow, friendsDF, followersDF)
	features[AVERAGE_NEIGHBORS_FOLLOWERS] 	= get_average_neighbors_followers(userID,friendsDF,usersDF)
	features[AVERAGE_NEIGHBORS_TWEETS] 		= get_average_neighbors_tweets(userID, usersDF,friendsDF, tweetsDF)
	#features[FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS] = get_followings_to_median(userRow)
	

def get_camisani_features(dataframes):
	camisaniFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		camisaniFeatures.append(get_single_user_camisani_features(row,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return camisaniFeatures

def get_single_user_camisani_features(userRow, tweetsDF):
	'''
	Class A : has name, has image, has address, has bio, followers >= 30, belongs to a list, 
	tweets >= 50, URL in profile, 2xfollowers >= friends

	Class B : geo, is favorite, uses punctuation, uses #, uses iphone, uses android, uses foursquare,
	uses twitter.com, userId in tweet, retweet >= 1, uses different clients
	'''

	features = {}

	# class A
	time("start")
	#t2 = time()
	features[HAS_NAME] 			= has_name(userRow)
	#print ("class A.1 camisani:", round(time()-t2, 3), "s")
	#t3 = time()
	features[HAS_IMAGE] 		= has_image(userRow)
	#print ("class A.2 camisani:", round(time()-t3, 3), "s")
	#t4 = time()
	features[HAS_ADDRESS] 		= has_address(userRow)
	#print ("class A.3 camisani:", round(time()-t4, 3), "s")
	#t5 = time()
	features[HAS_BIO] 			= has_bio(userRow)
	#print ("class A.4 camisani:", round(time()-t5, 3), "s")
	#t6 = time()
	features[HAS_30_FOLLOWERS] 	= has_30_followers(userRow)
	#print ("class A.5 camisani:", round(time()-t6, 3), "s")
	#t7 = time()
	features[BELONGS_TO_A_LIST] = belongs_to_a_list(userRow)
	#print ("class A.6 camisani:", round(time()-t7, 3), "s")
	#t8 = time()
	features[HAS_50_TWEETS] 	= has_50_tweets(userRow)
	#print ("class A.7 camisani:", round(time()-t8, 3), "s")
	#t9 = time()
	features[URL_IN_PROFILE] 	= url_in_profile(userRow)
	#print ("class A.8 camisani:", round(time()-t9, 3), "s")
	#t10 = time()
	features[FOLLOWERS_TO_FRIENDS_RATIO_OVER_2] = followers_to_friends_ration_over_2(userRow)
	#print ("class A.9 camisani:", round(time()-t10, 3), "s")
	#print ("class A camisani:", round(time()-t2, 3), "s")

	# class B
	#t1 = time()
	#t10 = time()
	features[GEOLOCALIZED] 				= geolocalized(userRow,tweetsDF)
	#print ("class B.1 camisani:", round(time()-t10, 3), "s")
	#t11 = time()
	features[IS_FAVORITE] 				= is_favorite(userRow,tweetsDF)
	#print ("class B.2 camisani:", round(time()-t11, 3), "s")
	#t12 = time()
	features[USES_PUNCTUATION] 			= uses_punctuation(userRow,tweetsDF)
	#print ("class B.3 camisani:", round(time()-t12, 3), "s")
	#t13 = time()
	features[USES_HASHTAG] 				= uses_hashtag(userRow,tweetsDF)
	#print ("class B.4 camisani:", round(time()-t13, 3), "s")
	#t14 = time()
	features[USES_IPHONE] 				= uses_iphone(userRow,tweetsDF)
	#print ("class B.5 camisani:", round(time()-t14, 3), "s")
	#t15 = time()
	features[USES_ANDROID] 				= uses_android(userRow,tweetsDF)
	#print ("class B.6 camisani:", round(time()-t15, 3), "s")
	#t16 = time()
	features[USES_FOURSQUARE] 			= uses_foursquare(userRow,tweetsDF)
	#print ("class B.7 camisani:", round(time()-t16, 3), "s")
	#t17 = time()
	features[USES_INSTAGRAM] 			= uses_instagram(userRow,tweetsDF)
	#print ("class B.8 camisani:", round(time()-t17, 3), "s")
	#t18 = time()
	features[USES_TWITTERDOTCOM] 		= uses_twitterdotcom(userRow,tweetsDF)
	#print ("class B.9 camisani:", round(time()-t18, 3), "s")
	#t19 = time()
	features[USERID_IN_TWEET] 			= userid_in_tweet(userRow,tweetsDF)
	#print ("class B.10 camisani:", round(time()-t19, 3), "s")
	#t20 = time()
	features[TWEETS_WITH_URL] 			= tweets_with_url(userRow,tweetsDF)
	#print ("class B.11 camisani:", round(time()-t20, 3), "s")
	#t21 = time()
	features[RETWEET_OVER_1] 			= retweet_over_1(userRow,tweetsDF)
	#print ("class B.12 camisani:", round(time()-t21, 3), "s")
	#t22 = time()
	features[USES_DIFFERENT_CLIENTS] 	= uses_different_clients(userRow,tweetsDF)
	#print ("class B.13 camisani:", round(time()-t22, 3), "s")
	#print ("class B camisani:", round(time()-t1, 3), "s")
	#print ("camisani:", round(time()-t0, 3), "s")
	time("end")
	return features

def get_state_of_search_features(dataframes):
	stateofsearchFeatures = []

	usersDF 	= dataframes['users']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		stateofsearchFeatures.append(get_single_user_state_of_search_features(row,usersDF,tweetsDF))

		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return stateofsearchFeatures


def get_single_user_state_of_search_features(userRow, usersDF, tweetsDF):
	'''
	Class A : bot in biography, friends/followers > 100, duplicate profile pictures

	Class B : same sentence to many accounts, tweet from API
	'''

	features = {}

	# class A
	#0 = time()
	#t1 = time()
	features[BOT_IN_BIO] 						= bot_in_bio(userRow)
	#print ("class A.1 stateofsearch:", round(time()-t1, 3), "s")
	#t2 = time()
	features[FRIENDS_TO_FOLLOWERS_RATIO_IS_100] = friends_to_followers_ratio_is_100(userRow)
	#print ("class A.2 stateofsearch:", round(time()-t2, 3), "s")
	#t3 = time()
	features[DUPLICATE_PROFILE_PICTURE] 		= duplicate_profile_picture(userRow,usersDF)
	#print ("class A.3 stateofsearch:", round(time()-t3, 3), "s")
	
	# class B
	#t4 = time()
	features[DUPLICATE_SENTENCES_ACROSS_TWEETS] 	= duplicate_sentences_across_tweets(userRow,tweetsDF)
	#print ("class B.1 stateofsearch:", round(time()-t4, 3), "s")
	#t5 = time()
	features[API_TWEETS] 							= api_tweets(userRow,tweetsDF)
	#print ("class B.2 stateofsearch:", round(time()-t5, 3), "s")
	#print ("stateofsearch:", round(time()-t0, 3), "s")

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

def get_single_user_socialbakers_features(userRow, friendsDF,tweetsDF):
	'''
	Class A : followers ≥ 50, default image after 2
		months, no bio, no location, friends ≥100, 0 tweets 
	
	Class B : tweets spam phrases, same tweet ≥ 3, retweets ≥ 90%,
		tweet-links ≥ 90%
	'''
	userID = userRow['id']

	features = {}

	#Class A

	#TODO : ce n'est pas 50 followers, c'est un ratio de 50:1 entre friends et followers
	features[HAS_50_FOLLOWERS] 	= has_50_followers(userRow)
	features[HAS_DEFAULT_IMAGE] = has_default_image(userRow)
	features[HAS_NO_BIO] 		= has_no_bio(userRow)
	features[HAS_NO_LOCATION] 	= has_no_location(userRow)
	features[HAS_100_FRIENDS] 	= has_100_friends(userRow)
	features[HAS_NO_TWEETS] 	= has_no_tweets(userID, tweetsDF)

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

	LIMIT = 5
	limit = 1

	for index, row in usersDF.iterrows():
		timelog("User "+str(limit))
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
	'''
	usersDF.set_index('id', inplace=True)
	tweetsDF.set_index('user_id',inplace=True)
	friendsDF.set_index('source_id', inplace=True)
	'''
	userID = userRow['id']

	features = {}

	# Class A
	features[NUMBER_OF_FRIENDS] 			= get_friends_count(userRow)
	features[FRIENDS_TO_FOLLOWERS_RATIO] 	= get_stringhini_friends_to_followers_ratio(userRow)

	# Class B
	features[NUMBER_OF_TWEETS_SENT]	= get_tweets_count(userID,tweetsDF)
	
	#features[TWEET_SIMILARITY] 	= get_tweet_similarity(userRow,tweetsDF)	#comment calculer?
	features[URL_RATIO] 		= get_url_ratio(userRow, tweetsDF)
	features[UNIQUE_FRIENDS_NAME_RATIO] = get_unique_friends_name_ratio(userID,usersDF,friendsDF) 

	return features

def get_yang_features(dataframes):
	yangFeatures = []

	usersDF 	= dataframes['users']
	friendsDF 	= dataframes['friends']
	followersDF = dataframes['followers']
	tweetsDF 	= dataframes['tweets']

	LIMIT = 10
	limit = 1

	for index, row in usersDF.iterrows():
		yangFeatures.append(get_single_user_yang_features(row, usersDF,friendsDF,followersDF,tweetsDF))

		timelog("User "+str(limit))
		
		#Temporary code, for test purpose
		if(limit > LIMIT):
			break
		else:
			limit = limit +1

	return yangFeatures


def get_single_user_yang_features(userRow, usersDF, friendsDF, followersDF,tweetsDF):
	'''
	class A : age, following rate

	Class B : API ratio, API URL ratio, API tweet similarity

	Class C: bi-link ratio, average
		neighbors’ followers, average
		neighbors’ tweets, followings
		to median neighbor’s followers
	'''
	userID = userRow['id']

	features = {}

	# Class A features
	features[ACCOUNT_AGE] 		= get_account_age(userRow)
	#features[FOLLOWING_RATE] 	= get_following_rate(userRow) # What is following rate?

	# Class B features
	#features[API_RATIO] 			= get_api_ratio(userRow)
	#features[API_URL_RATIO] 		= get_api_url_ratio(userRow)
	#features[API_TWEET_SIMILARITY] 	= get_api_tweet_similarity(userRow)

	# Class C features
	#features[BILINK_RATIO] 					= get_bilink_ratio(userRow, friendsDF, followersDF)
	features[AVERAGE_NEIGHBORS_FOLLOWERS] 	= get_average_neighbors_followers(userID,friendsDF,usersDF)
	features[AVERAGE_NEIGHBORS_TWEETS] 		= get_average_neighbors_tweets(userID, usersDF,friendsDF, tweetsDF)
	#features[FOLLOWINGS_TO_MEDIAN_NEIGHBORS_FOLLOWERS] = get_followings_to_median(userRow)

	return features

def get_dataframes(featureSetName, datasetDirectory):
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
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv','friends': 'friends.csv'
					,'followers': 'followers.csv'}

	elif(featureSetName == CLASS_A):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv'}

	elif(featureSetName == CLASS_C):
		fileNames = {'users' : 'users.csv', 'tweets' : 'tweets.csv','friends': 'friends.csv'
					,'followers': 'followers.csv'}

	# We load the dataframes from the files specified above, in a dataframe dictionary
	for key, filename in fileNames.items():

		totalPath = datasetDirectory + '/'+ filename
		
		timelog("Loading "+ totalPath)

		try:
			dataframes[key] = pd.read_csv(totalPath, encoding='latin-1').fillna('')
			#dataframes[key] = pd.read_csv(totalPath).fillna('')
		except Exception as e:
			print("Error while reading file "+totalPath)
			print(e)

	return dataframes 

'''
TODO: create functions that retrieve each individual feature, below
'''

# Class A features

def has_name(userRow):
	res = (not userRow['name'] == "")

	if(res):
		return 1
	else:
		return 0

def has_image(userRow):
	res = (not userRow['profile_image_url'] == "")

	if(res):
		return 1
	else:
		return 0

def has_address(userRow):
	res = (not userRow['location'] == "")

	if(res):
		return 1
	else:
		return 0

def has_bio(userRow):
	res =  (not userRow['description'] == "")

	if(res):
		return 1
	else:
		return 0

def has_30_followers(userRow):
	res = int(userRow['followers_count']) >= 30

	if(res):
		return 1
	else:
		return 0

def belongs_to_a_list(userRow):
	res = int(userRow['listed_count']) > 0

	if(res):
		return 1
	else:
		return 0

def has_50_tweets(userRow):
	res = userRow['statuses_count'] > 50

	if(res):
		return 1
	else:
		return 0

def url_in_profile(userRow):
	res = 0
	if isinstance(userRow['description'], str) and has_url(userRow['description']):
		res = 1
	return res

def followers_to_friends_ration_over_2(userRow):
	res =  int(userRow['followers_count'])/int(userRow['friends_count']) > 2

	if(res):
		return 1
	else:
		return 0

def bot_in_bio(userRow):
	# https://stackoverflow.com/questions/11144389/find-all-upper-lower-and-mixed-case-combinations-of-a-string
	bot_list = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in 'bot')))

	res = 0
	time("start")
	if isinstance(userRow['description'],str):
		for bot_combination in bot_list:
			if bot_combination in userRow['description']:
				res = 1
	time("end")

	return res

def friends_to_followers_ratio_is_100(userRow):
	threshold = 100

	res = get_friends_to_followers_ratio(userRow) >= threshold

	if(res):
		return 1
	else:
		return 0

def duplicate_profile_picture(userRow,usersDF):
	'''
	This functions checks if the name of the profile picture link is duplicated.
	'''
	clean = lambda x: x.split('/')[-1]
	image = userRow['profile_image_url'].split('/')[-1]
	img_column = usersDF['profile_image_url'].apply(clean)

	res = not image in img_column.unique()

	if(res):
		return 1
	else:
		return 0

def get_account_age(userRow):
	# Date format : Thu Apr 06 15:24:15 +0000 2017
	creation_date = userRow['created_at']
	
	account_creation = datetime.strptime(creation_date,'%a %b %d %H:%M:%S %z %Y')
	#Two lines below, to prevent error : can't subtract offset-naive and offset-aware datetimes
	# Solution from https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
	timezone = account_creation.tzinfo
	today = datetime.now(timezone)

	return (today - account_creation).days

def get_following_rate(userRow):
	'''
	following rate: this metric reflects the speed at which an
	accounts follows other accounts. Spammers usually feature high
	values of this rate.
	'''

	#how to calculate that?
	return 0

def get_friends_count(userRow):
	return int(userRow['friends_count'])

def get_friends_tweet_count(userRow,friendsDF,usersDF):
	friends_id_list = get_friends_ids(userRow['id'],friendsDF)

	friends_count = len(friends_id_list)

	return 0

def get_friends_to_followers_ratio(userRow):
	res = 0
	if int(userRow['followers_count']) != 0:
		int(userRow['friends_count'])/int(userRow['followers_count'])
	return res

def get_stringhini_friends_to_followers_ratio(userRow):
	followers = int(userRow['followers_count'])

	return int(userRow['friends_count'])/(followers*followers)

def has_50_followers(userRow):
	res = int(userRow['followers_count'])>= 50

	if(res):
		return 1
	else:
		return 0

def has_default_image(userRow):
	res =  userRow['default_profile_image']

	if(res):
		return 1
	else:
		return 0

def has_no_bio(userRow):
	if(not userRow['description']):
		return 1
	else:
		return 0

def has_no_location(userRow):
	if(not userRow['location']):
		return 1
	else:
		return 0

def has_100_friends(userRow):
	res =  get_friends_count(userRow) >= 100

	if(res):
		return 1
	else:
		return 0

def has_no_tweets(userID, tweetsDF):
	res = not has_tweets(userID, tweetsDF)

	if(res):
		return 1
	else:
		return 0


# Class B features
def geolocalized(userRow,tweetsDF):
	tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	geo = tweets['geo'] != ""
	res =  not tweets[geo].empty

	if(res):
		return 1
	else:
		return 0
	
def is_favorite(userRow,tweetsDF):
	tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	fav = tweets['favorite_count'] != 0
	return not tweets[fav].empty

def uses_punctuation(userRow,tweetsDF):
	# https://mail.python.org/pipermail/tutor/2001-October/009454.html
	bio_and_timeline = ""
	if isinstance(userRow['description'], str):
		bio_and_timeline += userRow['description']
	bio_and_timeline += get_tweets_strings(int(userRow['id']),tweetsDF)

	res = 0

	for letter in bio_and_timeline:
		if letter in string.punctuation:
			res = 1
	return res

def uses_hashtag(userRow,tweetsDF):
	return '#' in get_tweets_strings(int(userRow['id']),tweetsDF)

def uses_iphone(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return "Iphone" in all_tweets['source'].str.cat()

def uses_android(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return "Android" in all_tweets['source'].str.cat()

def uses_foursquare(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return "foursquare" in all_tweets['source'].str.cat()

def uses_instagram(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return "Instagram" in all_tweets['source'].str.cat()

def uses_twitterdotcom(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return "web" in all_tweets['source'].str.cat()
	
def userid_in_tweet(userRow,tweetsDF):
	return str(userRow['id']) in get_tweets_strings(userRow['id'],tweetsDF)

def tweets_with_url(userRow,tweetsDF):
	return has_url(get_tweets_strings(userRow['id'],tweetsDF))

def retweet_over_1(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	# Any checks if the conditions happens once in the Series.
	return (all_tweets['retweet_count'] > 1).any()

def uses_different_clients(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return len(all_tweets['source'].unique()) > 1

# https://stackoverflow.com/questions/17388213/find-the-similarity-percent-between-two-strings
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def duplicate_sentences_across_accounts(userRow,tweetsDF):
	return 0

def duplicate_sentences_across_tweets(userRow,tweetsDF):
	res = False
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	counter = 0
	for index, tweet in all_tweets.iterrows():
		other_counter = 0
		for other_index, other_tweet in all_tweets.iterrows():
			if similar(tweet['text'],other_tweet['text']) > 0.7 and index != other_index :
				res = True
				break
			if other_counter == 20:
				break
			other_counter+=1
		if counter == 20:
			break
		counter+=1		
	return res

def api_tweets(userRow,tweetsDF):
	all_tweets = get_tweets_dataframe_user(int(userRow['id']),tweetsDF)
	return not "twitter.com" in all_tweets['source'].str.cat()

def get_api_ratio(userRow):
	# tweets sent from api over total number of tweets
	return 0

def get_api_url_ratio(userRow):
	return 0

def get_api_tweet_similarity(userRow):
	return 0

def get_tweet_similarity(userID,tweetsDF):
	return 0

def get_url_ratio(userRow, tweetsDF):
	'''ratio of tweets with a url'''
	return get_tweets_with_url_ratio(userRow['id'],tweetsDF)

def get_unique_friends_name_ratio(userID,usersDF,friendsDF):
	friends_with_name = get_friends_with_initialized_name(userID, usersDF,friendsDF)
	unique_names_count = count_unique_names(friends_with_name)

	#avoid division by zero, so we return a big number
	if(unique_names_count == 0):
		return sys.maxsize

	return len(friends_with_name)/unique_names_count

def has_duplicate_tweets(userRow, tweetsDF,duplicate_threshold):
	return 0

def has_retweet_ratio(userRow,tweetsDF, ratio_threshold):
	'''
	Returns true if the ratio calculated is superior or equal to the ratio_threshold.
	Returns false otherwise.
	'''
	return 0

def has_tweet_links_ratio(userRow, tweetsDF, ratio_threshold):
	'''
	Returns true if the ratio calculated is superior or equal to the ratio_threshold.
	Returns false otherwise.
	'''
	return 0


# Class C featrues
def get_bilink_ratio(userRow, friendsDF, followersDF):
	userID = userRow['id']
	friends_count = userRow['friends_count']
	#Bi-directional link is when two account follow each other
	friends = get_friends_ids(userID,friendsDF)

	followersSeries = get_follower_ids(userID,followersDF)

	bilinkList = followersSeries.isin(friends).tolist()

	bilink_count = len(bilinkList)
	print("===== User ID = "+str(userID))
	print("[Bilink count : {}][Official Friends count : {}][Official Followers count :  {}], [followers actually found : {} ]".format(bilink_count,friends_count,userRow['followers_count'], len(followersSeries)))
	return bilink_count/friends_count

def get_average_neighbors_followers(userID,friendsDF,usersDF):
	#Average the number of followers of the friends of the user.
	friends = get_friends_ids(userID, friendsDF)

	return get_avg_neighbors_followers(friends,usersDF)

def get_average_neighbors_tweets(userID, userDF, friendsDF, tweetsDF):
	#Average the number of tweets of the friends of the user.
	friends = get_friends_ids(userID, friendsDF)
	return get_avg_friends_tweets(friends,tweetsDF)
	

def get_followings_to_median(userRow):
	'''
	Ratio between number of friends and the median of the followers of its friends.
	'''
	return 0

def timelog(message):
	print(datetime.now().strftime('%H:%M:%S')+' '+message )
'''
To use (prototype) go to root directory:
	command example : python3 src/features.py "data/E13/" yang
'''
if(__name__ == "__main__"):
	directory = sys.argv[1]

	featureSetName = sys.argv[2]
	dataframes = get_dataframes(directory,featureSetName)


	timelog("OK, ca passe")
	features 	= pd.DataFrame(get_features(featureSetName, dataframes))

	timelog("Features : ")
	print(features)
