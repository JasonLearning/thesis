#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 下午2:38
# @Author  : Aries
# @File    : svm.py
import numpy as np
import os
from sklearn import svm
from sklearn.externals import joblib
from train.helper import *

if __name__ == '__main__':
    print('start train model\n')
    # read raw_data&train_data
    raw_data = np.loadtxt('train_data.txt', delimiter=",")
    test_data = np.loadtxt('test_data.txt', delimiter=",")
    print('raw_data dimensions: ', str(len(raw_data)))
    print('test_data dimensions: ', str(len(test_data)))
    print('\n')

    # init & set parameters
    # set X as data of all
    X = raw_data[:, 0:4000]
    # set Y as result of all
    Y = raw_data[:, 4000]
    # set gamma like 1/n_features
    # in this case, n_features = 5806
    gamma = 0.0002
    # set C.the bigger the more accurate
    C = 100
    # set core function
    # linear u'v
    # poly (gamma*u'*v + coef0)^degree
    # rbf exp(-gamma|u'-v|^2)
    # sigmoid tauh(gamma*u'*v + coef0)
    kernel = 'rbf'
    # set tol
    tol = 0.005

    # simply train
    clf = svm.SVC(gamma=gamma, C=C, kernel=kernel, tol=tol)
    print('model')
    print(clf)
    print('\n')
    clf.fit(X, Y)

    # test model
    test_x = test_data[:, 0:4000]
    test_y = test_data[:, 4000]
    accuracy = test_model(clf, test_x, test_y)

    # save model
    # when using model, clf = joblib.load('filename.pk1')
    clf_name = 'svm_train_accuracy_{}.pk1'.format(accuracy)
    joblib.dump(clf, clf_name)
    print('save model as {}\n'.format(clf_name))
    print('end train')
