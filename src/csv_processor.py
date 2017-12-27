import sys
import pandas as pd 
import numpy as np 
import sklearn
import random
import matplotlib.pyplot as plt 

def get_dataframe(filename):
	df = None

	try:
		df = pd.read_csv(filename)

	except:
		print("Error while loading file : "+filename)

	return df

def HUM_creator(e13_folder,tfp_folder,hum_folder):
	"""
	Very simple compilation of the HUM datasets merging E13 and TFP.
	E13 count: 1481
	TFP count: 469
	final accounts: 1950
	"""
	files = ["users.csv","followers.csv","friends.csv","tweets.csv"]
	for file in files:
		f1 = open(e13_folder+file,"r", errors="ignore")
		f2 = open(tfp_folder+file,"r", errors="ignore")
		f3 = open(hum_folder+file,"w", errors="ignore")
		for lines in f1.readlines():
			f3.write(lines)

		for lines in f2.readlines()[1:]:
			f3.write(lines)
	f1.close()
	f2.close()
	f3.close()

def FAK_creator(fsf_folder,int_folder,twt_folder,fak_folder):
	"""
	From the dataset of fake accounts, we undersample the dataset randomly to 
	reach the same amout as the HUM dataset.
	FSF count: 1169
	INT count: 1337
	TWT count: 845
	fake accounts count: 3351
	final accounts needed: 1950
	percent randomly selected from the fake sample: 0.5819 
	"""
	file_merging(fsf_folder,int_folder,twt_folder,fak_folder,0.5819)

def file_merging(folder1,folder2,folder3,result_folder,percent):
	# 3 folders with fake accounts
	# 
	# In each folder we start by randomly undersampling the users
	# Then we use the ids collected for the users and fetch the corresponding data
	# in the other files.
	folder_list = [folder1,folder2,folder3]
	files = ["users.csv","followers.csv","friends.csv","tweets.csv"]

	for folder in folder_list:
		for file in files:
			f = open(folder+file,"r", errors="ignore")
			r = open(result_folder+file,"w",errors="ignore")
			
			len_file = len(f.readlines())
			print("length file: "+str(len_file))

			# choosing the number of lines we'll keep
			number_lines = int(percent*len_file)
			print("nb of lines: "+str(number_lines))

			# This creates a random sub-sample of the lines of the files
			# 
			# This works to select the percent of users we are interested but 
			# for the other files we have to select the corresponding data.
			
			list_of_ids = []

			if file == "users":
				for lines in random.sample(range(1,len_file+1), number_lines):
					list_of_ids.append(lines.split(",")[0])
					r.write(lines)
			else:
			# So after selecting the percent of users we want, we have to fetch the ids 
			# and collect the corresponding data in the other files.
				# for tweets.csv the id is the [3] element
				# for friends.csv the id is the [0] element
				# and for followers.csv the id is the [1] element
				for lines in f1.readlines()[1:]:
					if lines.split(",")[]

if(__name__ == "__main__"):
	#HUM_creator("../data/E13/","../data/TFP/","../data/HUM/")
	FAK_creator("../data/FSF/","../data/INT/","../data/TWT/","../data/FAK/")
	#BAS_creator("../data/HUM/","../data/FAK/","../data/BAS/")