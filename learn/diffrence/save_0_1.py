#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 下午1:16
# @Author  : Aries
# @File    : save_0_1.py

from documents.data_collection import DataCollection
from mongoengine import *
import pymysql
import numpy as np
from sklearn import datasets

digits = datasets.load_digits()

if __name__ == '__main__':
    db = pymysql.connect("localhost", "root", "jsl950511", "casco")
    cursor = db.cursor()
    with open('right_data.txt', 'w') as f:
        for i in np.arange(61000, 61030, 1):
            cursor.execute('SELECT * FROM train WHERE ID={i};'.format(i=i))
            data = cursor.fetchone()
            if data:
                print(data[0], data[5])
                sd = str(data[5])
                full_string = sd[2:-1]
                f.write(full_string)
                f1 = data[6]
                f.write(','+str(f1)+'\n')
    # with open('wrong_data.txt', 'w') as f:
    #     cursor.execute('SELECT * FROM train WHERE first_judge_machine=1;')
    #     datas = cursor.fetchall()
    #     for data in datas:
    #         if data:
    #             print(data[0], data[5])
    #             sd = str(data[5])
    #             full_string = sd[2:-1]
    #             f.write(full_string)
    #             f1 = data[6]
    #             f.write(','+str(f1)+'\n')
