import sys
import pandas as pd 
import numpy as np 
import sklearn
import matplotlib.pyplot as plt 

def get_dataframe(filename):
	df = None

	try:
		df = pd.read_csv(filename)

	except:
		print("Error while loading file : "+filename)

	return df

"""

Partie problématique de l'étude car manque de compréhension.


Although Twitter has never disclosed the total number of registered users, unofficial sources claim that
the Twitter accounts created up to date are many more than the MAUs. This is why we made a conservative
assumption, considering a balanced distribution of fake followers and human followers as our baseline dataset.
9
To validate this assumption, we performed the experiments in [34] to our dataset. We progressively varied the
class distribution of fake followers and human followers in the dataset, from 5%–95% to 95%–5% (respectively
100 humans–1900 fake followers, 1900 humans–100 fake followers), and used the obtained dataset to train
J48 classifiers, considering their performances with cross-validation. The trained classifiers obtained their
best results on a balanced distribution of humans and fake followers. To obtain a balanced dataset, we
randomly undersampled the total set of fake accounts (i.e., 3351) to match the size of the HUM dataset of
verified human accounts. Thus, we built a baseline dataset of 1950 fake followers, labeled FAK


"""


def HUM_creator(e13_folder,tfp_folder):
	"""
	Very simple compilation of the HUM datasets merging E13 and TFP.
	E13 count: 1481
	TFP count: 469
	final accounts: 1950
	"""


def FAK_creator(fsf_folder,int_folder,twt_folder):
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

def file_merging(folder1,folder2,percent=100):
	files = ["followers.csv","friends.csv","tweets.csv","users.csv"]
	for file in files:
		f1 = open(folder1+file,"r")
		f2 = open(folder2+file,"w")




if(__name__ == "__main__"):
	args = sys.argv[1:]
	print(sys.argv)
	if(len(args) == 1):
		main(args[0],None)
	elif(len(args) == 2):
		main(args[0], args[1])
	else:
		print("Argument missing : Filename required")