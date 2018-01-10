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
from sklearn.model_selection import cross_val_score
 from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from pomegranate import *
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm


def random_forest():
	# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
	# 
	# RandomForestClassifier(n_estimators=10, criterion=’gini’, 
	# max_depth=None, min_samples_split=2, min_samples_leaf=1, 
	# min_weight_fraction_leaf=0.0, max_features=’auto’, 
	# max_leaf_nodes=None, min_impurity_decrease=0.0, 
	# min_impurity_split=None, bootstrap=True, oob_score=False, 
	# n_jobs=1, random_state=None, verbose=0, warm_start=False, 
	# class_weight=None)
	# 
	# clf = RandomForestClassifier(max_depth=2, random_state=0)
	# clf.fit(X, y)
	# clf.predict([[0, 0, 0, 0]]))
	pass

def decorate():
	# Install https://github.com/fracpete/python-weka-wrapper3
	# 
	# examples: https://github.com/fracpete/python-weka-wrapper3-examples/blob/master/src/wekaexamples/classifiers/classifiers.py
	# pass
	# load a dataset
    loader = Loader("weka.core.converters.ArffLoader")

    #evaluation
    evaluation = Evaluation(train_features)


def decision_tree():
	# http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier
	# clf = DecisionTreeClassifier(random_state=0)
	#
	# DecisionTreeClassifier(criterion=’gini’, splitter=’best’, 
	# max_depth=None, min_samples_split=2, min_samples_leaf=1, 
	# min_weight_fraction_leaf=0.0, max_features=None, 
	# random_state=None, max_leaf_nodes=None, 
	# min_impurity_decrease=0.0, min_impurity_split=None, 
	# class_weight=None, presort=False)
	# J48
	clf = train_decision_tree(train_features,train_labels)
	
	result = cls.score(test_features, test_labels)

	return clf

def train_decision_tree(train_features, train_labels):
	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(train_features, train_labels)


def adaptive_boost():
	# http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html
	# 
	# AdaBoostClassifier(base_estimator=None, n_estimators=50, 
	# learning_rate=1.0, algorithm=’SAMME.R’, random_state=None)
	#
	# iris = load_iris()
	# clf = AdaBoostClassifier(n_estimators=100)
	# scores = cross_val_score(clf, iris.data, iris.target)
	# scores.mean()   
	clf = AdaBoostClassifier(n_estimators=100, learning_rate=0.1)


def bayesian_network():
	# http://pomegranate.readthedocs.io/en/latest/BayesianNetwork.html
	# Careful with dependencies
	# 
	model = BayesianNetwork.from_samples(train_features, algorithm='exact')
	model.predict(test_features)

def k_nearest_neighbors():
	# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
	#
	# neigh = KNeighborsClassifier(n_neighbors=3)
	# neigh.fit(X, y)
	# print(neigh.predict([[1.1]]))
	# 
	# (n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30,
	#  p=2, metric=’minkowski’, metric_params=None, n_jobs=1, **kwargs)
	pass

def logistic_regression():
	# http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
	# 
	# LogisticRegression(penalty=’l2’, dual=False, tol=0.0001, C=1.0,
	# fit_intercept=True, intercept_scaling=1, class_weight=None, 
	# random_state=None, solver=’liblinear’, max_iter=100, 
	# multi_class=’ovr’, verbose=0, warm_start=False, n_jobs=1)
	# 
	# clf = LogisticRegression()
	# clf.fit(X, y)
	# clf.predict(X)
	# 
	pass

def support_vector_machine():
	clf = svm.SVC(kernel='rbf',C=1.0,gamma=auto)
	#clf.fit(train_features, train_labels) 
	# clf.predict([[2., 2.]])
	# 
	# Algo: libSVM (SVC)
	# kernel: rbf
	# C 	: optimized 
	# gamma : optimized 
	# http://scikit-learn.org/stable/modules/grid_search.html
	# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV
	# http://scikit-learn.org/stable/auto_examples/svm/plot_rbf_parameters.html
	# 
	# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    # decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    # max_iter=-1, probability=False, random_state=None, shrinking=True,
    # tol=0.001, verbose=False)
    return clf

def classify(features_dataframe):

	# CROSS VALIDATION: cross_val_score(clf, test_features, test_labels, cv=10)
	# or 
	# from sklearn.model_selection import cross_val_predict
	# pred = cross_val_predict(clf, test_features, test_labels)

	features, labels = preprocess()

	# dico with the classifiers 
	classifiers_dict = {}
	# dico with the predictions made with the 
	predictions_dict = {}

	classifiers_dict['RF'] = random_forest()
	classifiers_dict['D'] = decorate()
	classifiers_dict['J48'] = decision_tree()
	classifiers_dict['AB'] = adaptive_boost()
	classifiers_dict['BN'] = bayesian_network()
	classifiers_dict['kNN'] = k_nearest_neighbors()
	classifiers_dict['LR'] = logistic_regression()
	classifiers_dict['SVM'] = support_vector_machine()

	for key, value in classifiers_dict.items():
		predictions_dict[key] = cross_val_predict(value, features, labels, cv=10)

	return predictions_dict


def preprocess():
	# 1. charger les 2 datasets(labelisés)
	# 2. concatener les 2
	pass