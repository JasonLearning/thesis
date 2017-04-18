#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 下午3:19
# @Author  : Aries
# @File    : helper.py


def test_model(clf, data, target):
    answer = clf.predict(data)
    right_num = 0
    total_num = 0
    print('----------start     test----------')
    for i in range(len(answer)):
        if answer[i] == target[i]:
            right_num += 1
        total_num += 1
    print('----------finish    test----------')
    print("----------test {} data----------".format(total_num))
    print("----------pass {} data----------".format(right_num))
    print("----------fail {} data----------".format(total_num-right_num))
    print('\n')
    return str(float(float(right_num) / float(total_num)) * 100) + '%'
