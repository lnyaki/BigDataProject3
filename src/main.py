from classifiers import *
from features import *
from metrics import *
import sys
from generateBAS import *

def main():
	

	# data frame with our dataset
	labels_A, labels_C, df_features_class_A, df_features_class_C = get_BAS_dataset("data/HUM/","data/FAK/")
	# preprocessing of the data to capture the features we want
	#df_features_class_A = get_class_A_features(df)
	#df_features_class_C = get_class_C_features(df)
	
	# classifiers (training + prediction)
	class_A_classifiers_predictions = classify(df_features_class_A,labels_A)
	class_C_classifiers_predictions = classify(df_features_class_C,labels_C)

	# Metrics on the result predictions from the classifiers
	results_class_A_classifiers = metrics(labels_A, class_A_classifiers_predictions)
	results_class_C_classifiers = metrics(labels_C, class_C_classifiers_predictions)
 
	# publish and save results
	print("Metrics of the Class A classifiers(profile)")
	for key,value in results_class_A_classifiers.items():
		print("Algorithm: "+key)
		print("Accuracy: "+ str(round(value[0],3))+ " Precision: "+str(round(value[1],3)))
		print("Recall: "+ str(round(value[2],3))+ " F-M: "+str(round(value[3],3)))
		print("MCC: "+ str(round(value[4],3))+ " AUC: "+str(round(value[5],3)))
		print()
	#publish(results_class_A_classifiers)
	print("===================== oOo ========================")
	print("Metrics of the Class C classifiers(all features)")
	for key,value in results_class_C_classifiers.items():
		print("Algorithm: "+key)
		print("Accuracy: "+ str(round(value[0],3))+ " Precision: "+str(round(value[1],3)))
		print("Recall: "+ str(round(value[2],3))+ " F-M: "+str(round(value[3],3)))
		print("MCC: "+ str(round(value[4],3))+ " AUC: "+str(round(value[5],3)))
		print()
	#publish(results_class_C_classifiers)


if(__name__ == "__main__"):
	# Command example. Load class A : python3 src/main.py data/E13 A
	# Command example. Load class C : python3 src/main.py data/E13 C

	#Get the dataset name (E13, FAK, FSF,HUM,etc)
	#baseDataset 	= sys.argv[1]
	#featureSetName 	= sys.argv[2]

	#dataframes  = features.get_dataframes(baseDataset_A, featureSetName)

	#main(baseDataset)
	main()

