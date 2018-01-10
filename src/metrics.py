from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import roc_curve
def metrics(labels,pred_dict):

	results_dict = {}
	# Confusion matrix
	# labels : array, shape = [n_samples]
	# Ground truth (correct) target values.
	# pred : array, shape = [n_samples]
	# Estimated targets as returned by a classifier.
	
	for key,pred in pred_dict.items():

		#tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
		#np.set_printoptions(precision=2)

		# Accuracy
		
		acc = accuracy_score(labels, pred)

		# Precision
		
		pres = precision_score(labels, pred, average='binary')

		# Recall
		
		rec = recall_score(labels, pred, average='binary')

		# F-measure
		
		f1 = f1_score(labels, pred, average='binary')

		# MCC
		
		mcc = matthews_corrcoef(labels, pred) 

		# AUC
		fpr, tpr, thresholds = roc_curve(y, pred, pos_label=2)
		auc_score = metrics.auc(fpr, tpr)
		# 
		# Coud be this one must be rechecked with paper
		# from sklearn.metrics import roc_auc_score
		# roc_auc_score(labels, y_scores)
		results_dict['key'] = [acc,pres,rec,f1,mcc,auc_score]
	return results_dict