#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/12 上午11:45
# @Author  : Aries
# @File    : mysql_to_mongodb.py

import pymysql
from mongoengine import *
from learn.plot_sin import DataCollection
from learn.plot_sin import DataCollectionClass
import numpy as np

if __name__ == '__main__':
    db_name = 'casco'
    connect(db_name)
    db = pymysql.connect("localhost", "root", "jsl950511", "casco")
    cursor = db.cursor()
    for i in np.arange(45921, 190641, 1):
        cursor.execute('SELECT * FROM train WHERE ID={i};'.format(i=i))
        data = cursor.fetchone()
        if data:
            print(data[0], data[5])
            sd = str(data[5])
            full_string = sd[2:-1].split(',')
            full_list = []
            for number in full_string:
                full_list.append(int(number))
            p = full_list[:1000]
            a = full_list[1000:2000]
            b = full_list[2000:3000]
            c = full_list[3000:]
            id = data[0]
            man = data[4]
            f = data[2]
            d = data[3]
            f1 = data[6]
            f2 = data[7]
            s1 = data[8]
            s2 = data[9]
            DataCollectionClass.insert(id, p, a, b, c, f, d, man, f1, f2, s1, s2)
