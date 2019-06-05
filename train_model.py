import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
import os

import pickle

from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.utils.multiclass import unique_labels

from string import ascii_lowercase, ascii_uppercase
from sklearn import preprocessing
alp = {}

for i in range(10):
    alp[str(30 + i)] = i

for i in range(9):
    alp[str(41 + i)] = ascii_uppercase[i]
for i in range(10):
    j = i + 15
    alp[str(50 + i)] = ascii_uppercase[j]
for i in range(9):
    alp[str(61 + i)] = ascii_lowercase[i]
for i in range(10):
    j = i + 15
    alp[str(70 + i)] = ascii_lowercase[j]
alp['7a'] = 'z'
alp['5a'] = 'Z'
j = 0
for i in ['a', 'b', 'c', 'd', 'e', 'f']:
    alp['4' + i] = ascii_uppercase[9 + j]
    j += 1
j = 0
for i in ['a', 'b', 'c', 'd', 'e', 'f']:
    alp['6' + i] = ascii_lowercase[9 + j]
    j += 1

txt_files = os.listdir('dataset')

x, y = [], []
x_pt, y_pt = [], []
n_pu = 1500
n_pt = 100
for file in txt_files:
    temp_arr = np.loadtxt('dataset/' + file, delimiter=' ')
    #indx = np.random.choice(temp_arr.shape[0], n_pu + n_pt, replace=False)
    x.append(temp_arr[:n_pu])
    y.append([file[:2]] * n_pu)
    x_pt.append(temp_arr[n_pu:n_pu + n_pt])
    y_pt.append([file[:2]] * n_pt)
x = np.array(x)
y = np.array(y)
x_pt = np.array(x_pt)
y_pt = np.array(y_pt)


y = y.reshape(y.shape[0] * y.shape[1])
x = x.reshape(x.shape[0] * x.shape[1], x.shape[2])
y_pt = y_pt.reshape(y_pt.shape[0] * y_pt.shape[1])
x_pt = x_pt.reshape(x_pt.shape[0] * x_pt.shape[1], x_pt.shape[2])


x = preprocessing.scale(x)
x_pt = preprocessing.scale(x_pt)

x_mean = np.mean(x, axis=1)
x_std = np.std(x, axis=1)
x_mean = x_mean.reshape(x_mean.shape[0], 1)
x_std = x_std.reshape(x_std.shape[0], 1)

x = x - x_mean
x = x / x_std

clf = svm.SVC(gamma=0.001, C=100)

clf.fit(x, y)

filename = 'finalized_model1500.sav'
pickle.dump(clf, open(filename, 'wb'))

y_predict = clf.predict(x_pt)

print(confusion_matrix(y_pt, y_predict, labels=list(alp.keys())))
print(accuracy_score(y_pt, y_predict))
