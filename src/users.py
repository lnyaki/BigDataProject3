import pandas as pd
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
	friendsIDs 	= get_friends_ids(userID,friendsDF)
	not_empty 	= usersDF['name'] != ''
	not_null 	= usersDF['name'].notnull()
	is_unique 	= usersDF['id'].isin(friendsIDs)

	return usersDF[not_null	& not_empty & is_unique]

def count_unique_names(friendsDF):
	#duplicate Dataframe
	friends2 = friendsDF.copy()
	unique_count = 0
	unique_names = friendsDF.name.unique()

	for index, row in friendsDF.iterrows():

		if(row['name'] in unique_names):
			unique_count = unique_count +1

	return unique_count

def get_avg_neighbors_followers(friendsIDlist,usersDF):
	friends_count 			= len(friendsIDlist)
	total_followers_count 	= 0

	userOK = 0
	userKO = 0

	for friendID in friendsIDlist:
		singleUserDF 	= usersDF[usersDF['id']== friendID]
		followers_count = 0

		if(singleUserDF.empty):
			userKO = userKO +1

		else:
			userOK = userOK +1
			
			total_followers_count = total_followers_count+ int(singleUserDF['followers_count'])

	print("[Total friends : {}], [friends found : {}], [missing friends :{}]".format(friends_count,userOK,userKO))

	if(userOK == 0):
		return 0
	else:
		return total_followers_count/userOK


