import pandas as pd
import cachedata as cache
'''
This module handles all processings on the friends of a user.
'''

def get_average_followers_count(userID, usersDF):
	pass
	#return usersDF

def get_friends_ids(userID, friendsDF):
	return friendsDF['target_id'][friendsDF['source_id'] == userID].tolist()

def get_follower_ids(userID, followersDF):
	#source = follower, target = user
	return followersDF['source_id'][followersDF['target_id'] == userID]
	#return followersDF['target_id'][followersDF['source_id'] == userID]

def get_friends_count(userID,friendsDF):
	return friendsDF[friendsDF['source_id'] == userID].count()

def get_friends_with_initialized_name(userID, usersDF, friendsDF):
	friendsIDs 	= cache.get_user_friends(userID,friendsDF)
	not_empty 	= usersDF['name'] != ''
	not_null 	= usersDF['name'].notnull()
	is_unique 	= usersDF['id'].isin(friendsIDs)

	return usersDF[not_null	& not_empty & is_unique]

def count_unique_names(friendsDF):
	#duplicate Dataframe
	
	unique_count = len(friendsDF.name.unique().tolist())	

	return unique_count

def get_avg_neighbors_followers(friendsIDlist,usersDF):
	friends_count 			= len(friendsIDlist)
	total_followers_count 	= 0

	friendsSeries = pd.Series(friendsIDlist)

	followers = usersDF['followers_count'][usersDF['id'].isin(friendsSeries)]
	total_followers_count = followers.shape[0]
	total_result = followers.sum()


	print("[Total friends : {}], [Followers : {}], [Total neigbors followers :{}]".format(friends_count,total_followers_count,total_result))

	if(total_followers_count == 0):
		return 0
	else:
		return total_result/total_followers_count


