import classifiers
import features
import metrics
import sys

def main(datasetDirectory):
	# data frame with our dataset
	df = get_BAS_dataset()

	# preprocessing of the data to capture the features we want
	df_features_class_A = get_class_A_features(df)
	df_features_class_C = get_class_C_features(df)

	

	# classifiers (training + prediction)
	class_A_classifiers_predictions = classify(df_features_class_A)
	class_C_classifiers_predictions = classify(df_features_class_C)

	# Metrics on the result predictions from the classifiers
	results_class_A_classifiers = metrics(labels,class_A_classifiers_predictions)
	results_class_C_classifiers = metrics(labels, class_C_classifiers_predictions)
 
	# publish and save results
	publish(results_class_A_classifiers)
	publish(results_class_C_classifiers)


if(__name__ == "__main__"):
	# Command example. Load class A : python3 src/main.py data/E13 A
	# Command example. Load class C : python3 src/main.py data/E13 C

	#Get the dataset name (E13, FAK, FSF,HUM,etc)
	baseDataset 	= sys.argv[1]
	featureSetName 	= sys.argv[2]

	dataframes  = features.get_dataframes(baseDataset_A, featureSetName)

	main(baseDataset)

