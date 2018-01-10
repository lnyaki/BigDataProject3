import pandas as pd
import features
import sys

'''
The goal of this module is to generate a list of features based on a
base directory (ex: E13, FAK, etc) and the name of the feature set (class A, class C).

The generated list is the baseline feature set and will be created in the directory
specified in parameters. Ex: E13/baseline.csv
'''

if(__name__ == "__main__"):
	# Command example. Load class A : python3 src/main.py data/E13 A
	# Command example. Load class C : python3 src/main.py data/E13 C

	#Get the dataset name (E13, FAK, FSF,HUM,etc)
	datasetDirectory 	= sys.argv[1]
	featureSetName 	= sys.argv[2]

	dataframes  	= features.get_dataframes(featureSetName,datasetDirectory)
	featuresData 	= features.get_features(featureSetName, dataframes)

	featuresData = pd.DataFrame(featuresData)

	print("features data :")

	print(featuresData)