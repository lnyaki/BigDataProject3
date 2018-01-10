from sklearn.metrics import confusion_matrix

# Confusion matrix

# y_true : array, shape = [n_samples]
# Ground truth (correct) target values.
# y_pred : array, shape = [n_samples]
# Estimated targets as returned by a classifier.

#tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
#np.set_printoptions(precision=2)

# Accuracy
# from sklearn.metrics import accuracy_score
# accuracy_score(y_true, y_pred)

# Precision
# from sklearn.metrics import precision_score
# precision_score(y_true, y_pred, average='binary')

# Recall
# from sklearn.metrics import recall_score
# recall_score(y_true, y_pred, average='binary')

# F-measure
# from sklearn.metrics import f1_score
# f1_score(y_true, y_pred, average='binary')

# MCC
# from sklearn.metrics import matthews_corrcoef
# matthews_corrcoef(y_true, y_pred) 

# AUC
# from sklearn import metrics
# fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
# metrics.auc(fpr, tpr)
# 
# Coud be this one must be rechecked with paper
# from sklearn.metrics import roc_auc_score
# roc_auc_score(y_true, y_scores)

# TODO: CROSS VALIDATION