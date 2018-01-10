import pandas as pd
import features
import sys
import os
from time import time

'''
The goal of this module is to generate a list of features based on a
base directory (ex: E13, FAK, etc) and the name of the feature set (class A, class C).

The generated list is the baseline feature set and will be created in the directory
specified in parameters. Ex: E13/baseline.csv
'''

def get_BAS_dataset(hum_path,fak_path):
	filename_A = "features_A.csv"
	filename_C = "features_C.csv"

	hum_df_A = pd.read_csv(hum_path+filename_A, encoding='latin-1',sep='\t')
	fak_df_A = pd.read_csv(fak_path+filename_A, encoding='latin-1',sep='\t')
	hum_df_C = pd.read_csv(hum_path+filename_C, encoding='latin-1',sep='\t')
	fak_df_C = pd.read_csv(fak_path+filename_C, encoding='latin-1',sep='\t')
	
	frames_A = [hum_df_A,fak_df_A]
	frames_C = [hum_df_C,fak_df_C]

	df_A = pd.concat(frames_A)
	df_C = pd.concat(frames_C)

	# randomize features, before cross_validation
	df_A = df_A.sample(frac=1).reset_index(drop=True)
	df_C = df_C.sample(frac=1).reset_index(drop=True)

	labels_A = df_A['label'].tolist()
	labels_C = df_C['label'].tolist()
	return labels_A,labels_C,df_A,df_C


def save_features_in_file(path, featuresDF, featureSetName):

	filename =  path + "/features_"+featureSetName+".csv"
	print("Current directory :"+os.getcwd())
	print("Filename : "+filename)
	featuresDF.to_csv(filename,sep='\t')

def labelize_features(featuresDF, label):
	labelVal = 0

	if(label == 'human'):
		labelVal = 0
	elif(label == 'bot'):
		labelVal = 1
		
	featuresDF['label'] = labelVal


if(__name__ == "__main__"):
	# Command example. Load class A : python3 src/main.py data/E13 A
	# Command example. Load class C : python3 src/main.py data/E13 C

	#Get the dataset name (E13, FAK, FSF,HUM,etc)
	argsLen = len(sys.argv)

	datasetDirectory 	= sys.argv[1]
	featureSetName 		= sys.argv[2]



	dataframes  	= features.get_dataframes(featureSetName,datasetDirectory)

	print("=========== Getting features ===========")
	print(time())
	t0 = time()
	
	featuresData 	= features.get_features(featureSetName, dataframes)

	featuresData = pd.DataFrame(featuresData)

	if(argsLen > 3):
		label 				= sys.argv[3]
		labelize_features(featuresData,label)

	tf = time() - t0
	print("========== Elapsed time ==========")
	print(tf)
	save_features_in_file(datasetDirectory, featuresData,featureSetName)
