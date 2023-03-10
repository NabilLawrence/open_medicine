#------------------------------------------------------
# Regular modules
#------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
#------------------------------------------------------
# Created module
#------------------------------------------------------
from Classifier import classifier_fake_real
#------------------------------------------------------
# Using the fake medical reports classifier
#------------------------------------------------------
feature_matrix_list = classifier_fake_real("OGD_FakeSet.csv",
                                           "OGD_FakeSet.csv")
#------------------------------------------------------
np.save('feature_matrix_list.npy', np.array(feature_matrix_list, dtype=object), allow_pickle=True)
feature_matrix_list_loaded = np.load('feature_matrix_list.npy', allow_pickle=True)
[X_train,X_valid,X_test,y_train,y_valid,y_test]=feature_matrix_list_loaded
#--------------------------------------------------------------------
# Training a classifier
#--------------------------------------------------------------------
lr_clf = LogisticRegression(max_iter=100)
lr_clf.fit(X_train, y_train)
#-----------------------------------------------------
print('CLASSIFIER MODEL TRAINED')
#--------------------------------------------------------------------
score=lr_clf.score(X_valid, y_valid)
#-----------------------------------------------------
print('SCORE:', score)
#--------------------------------------------------------------------
y_preds = lr_clf.predict(X_test)
cm = confusion_matrix(y_test, y_preds, normalize="true")
#-----------------------------------------------------
print('CONFUSION MATRIX:', cm)
#-----------------------------------------------------
print('CLASSIFIER EVALUATED')
#-----------------------------------------------------
