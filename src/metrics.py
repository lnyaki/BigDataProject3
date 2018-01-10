from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import roc_auc_score
def metrics(labels,pred_dict):

	results_dict = {}
	# Confusion matrix
	# labels : array, shape = [n_samples]
	# Ground truth (correct) target values.
	# pred : array, shape = [n_samples]
	# Estimated targets as returned by a classifier.
	
	for key,pred in pred_dict.items():
		#try:
			#tn, fp, fn, tp = confusion_matrix(y_test, pred).ravel()
			#np.set_printoptions(precision=2)
		try:
			# Accuracy
			acc = accuracy_score(labels, pred)
		except ValueError:
			acc = 0
		try:
			# Precision
			pres = precision_score(labels, pred, average='binary')
		except ValueError:
			pres = 0
		try:
			# Recall
			rec = recall_score(labels, pred, average='binary')
		except ValueError:
			rec = 0
		try:
			# F-measure
			f1 = f1_score(labels, pred, average='binary')
		except ValueError:
			f1 = 0
		try:
			# MCC
			mcc = matthews_corrcoef(labels, pred) 
		except ValueError:
			mcc = 0
		try:
			# AUC
			auc_score = roc_auc_score(labels, pred)
		except ValueError:
			auc_score = 0
			# 
			# Coud be this one must be rechecked with paper
			# from sklearn.metrics import roc_auc_score
			# roc_auc_score(labels, y_scores)
			results_dict[key] = [acc,pres,rec,f1,mcc,auc_score]
	#except ValueError:
	#	pass
	return results_dict