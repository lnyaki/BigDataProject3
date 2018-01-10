import tweets as tw
import users as us


_user_tweets = {}
_user_friends = {}
_user_followers = {}

_user_tweets_count = {}
_user_friends_count = {}
_user_followers_count = {}


def get_user_tweets(userID, tweetsDF):
	tweets = None
	try:
		tweets = _user_tweets[userID]

	except KeyError:
		_user_tweets[userID] = tw.get_tweets_dataframe_user(userID, tweetsDF)

	finally:
		tweets = _user_tweets[userID]

	return tweets

def get_tweets_count(userID, tweetsDF):
	tweetCount = 0

	try:
		tweetCount = _user_tweets_count[userID]

	except KeyError:
		_user_tweets_count[userID] = get_user_tweets(userID,tweetsDF).shape[0]

	finally:
		tweetCount = _user_tweets_count[userID]

	return tweetCount

def get_user_friends(userID, friendsDF):
	friends = None

	try:
		friends = _user_friends[userID]

	except KeyError:
		_user_friends[userID] = us.get_friends_ids(userID, friendsDF)

	finally:
		friends = _user_friends[userID]

	return friends

def get_friends_count(userID, friendsDF):
	friendsCount = 0

	try:
		userCount = _user_friends_count[userID]

	except KeyError:
		_user_friends_count[userID] = len(get_user_friends(userID,tweetsDF))

	finally:
		friendsCount = _user_friends_count[userID]

	return friendsCount

def get_user_followers(userID, followersDF):
	followers = None
	
	try:
		friends = _user_friends[userID]

	except KeyError:
		_user_followers[userID] = us.get_followers_ids(userID, followersDF)

	finally:
		followers = _user_followers[userID]

	return followers 

def get_followers_count(userID, followersDF):
	followersCount = 0

	try:
		followersCount = _user_followers_count[userID]

	except KeyError:
		_user_followers_count[userID] = len(get_user_followers(userID,tweetsDF).tolist())

	finally:
		followersCount = _user_followers_count[userID]

	return followersCount