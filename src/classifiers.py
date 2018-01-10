# References for this section
# 
# Classifiers used to evaluate the features
# Decorate (D), Adaptive Boost (AB), Random Forest (RF), 
# Decision Tree (J48), Bayesian Network (BN), k-Nearest Neighbors (kNN), 
# Multinomial Ridge Logistic Regression (LR) and a Support Vector
# Machine (SVM).
# 
# D, RF, J48 and BN
# -----------------
# http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.414.5888&rep=rep1&type=pdf
# ->  (http://puu.sh/yVTDB/41ec806328.png)
# Nothing special mentioned concerning the parameters for these 
# classifiers.
# 
# http://www.cse.iitd.ernet.in/~siy117527/sil765/readings/Detecting%20spammer%20on%20social%20network.pdf
# Again no information about the RF configuration
# 
# SVM
# ---
# Our SVM classifier exploits a Radial Basis Function (RBF) kernel
# and has been trained using libSVM as the machine learning algorithm
# The cost and gamma parameters have been optimized via a grid search 
# algorithm.
# 
# kNN
# ---
# k parameter of the kNN classifier and the ridge penalizing parameter
# of the LR model have been optimized via a cross validation parameter 
# selection algorithm.
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm

def random_forest(features):
	pass

def decorate(features):
	pass

def decision_tree(features):
	# J48
	pass

def adaptive_boost(features):
	pass

def bayesian_network(features):
	# http://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html
	# Careful with dependencies
	pass

def knn(features):
	# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
	#
	# neigh = KNeighborsClassifier(n_neighbors=3)
	# neigh.fit(X, y)
	# print(neigh.predict([[1.1]]))
	# 
	# (n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30,
	#  p=2, metric=’minkowski’, metric_params=None, n_jobs=1, **kwargs)
	pass

def logistic_regression(features):
	# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
	# http://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
	# 
	# LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0,
	# fit_intercept=True, intercept_scaling=1, class_weight=None, 
	# random_state=None, solver=’liblinear’, max_iter=100, 
	# multi_class=’ovr’, verbose=0, warm_start=False, n_jobs=1)
	pass

def svm(features):
	# clf = svm.SVC()
	# clf.fit(X, y) 
	# clf.predict([[2., 2.]])
	# 
	# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    # decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    # max_iter=-1, probability=False, random_state=None, shrinking=True,
    # tol=0.001, verbose=False)
    pass
