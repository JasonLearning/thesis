# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 17/4/10 上午11:53
# @Author   : Jason
# @File     : plot_sin.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mongoengine import *


class DataCollection(Document):
    p = ListField()
    a = ListField()
    b = ListField()
    c = ListField()
    isManmade = IntField()
    first_judge_machine = IntField()
    first_judge_artificial = IntField()
    second_judge_machine = IntField()
    second_judge_artificial = IntField()


class ShopListJobCollectionClass:
    def __init__(self):
        self.db_name = "casco"
        connect(self.db_name)

    @staticmethod
    def insert(p, a, b, c, man, f1, f2, s1, s2):
        DataCollection(
            p=p,
            a=a,
            b=b,
            c=c,
            isManmade=man,
            first_judge_machine=f1,
            first_judge_artificial=f2,
            second_judge_machine=s1,
            second_judge_artificial=s2
        ).save()


def deal_csv():
    file = 'casco_train.csv'
    total = pd.read_csv(file)
    for i in range(160000):
        sd = total['switch_data'][i]
        full_string = sd[2:-1].split(',')
        full_list = []
        for number in full_string:
            full_list.append(int(number))
        p = full_list[:1000]
        a = full_list[1000:2000]
        b = full_list[2000:3000]
        c = full_list[3000:]
        man = total['isManmade'][i]
        f1 = total['first_judge_machine'][i]
        f2 = total['first_judge_artificial'][i]
        s1 = total['second_judge_machine'][i]
        s2 = total['second_judge_artificial'][i]
        bsbsbs = ShopListJobCollectionClass()
        bsbsbs.insert(p, a, b, c, man, f1, f2, s1, s2)


def draw_sin():
    s = [1, 2, 3]
    t = np.array(s)
    y = np.array(s)
    z = np.cos(2 * np.pi * t / 256)
    plt.plot(t, y, 'black')
    plt.show()
    plt.plot(t, z, 'red')
    plt.show()


def draw_wave(switch_data):
    color = ['black', 'blue', 'red']
    t = np.arange(0, 10, 0.01)
    data = switch_data
    plt.plot(t, data, 'black')


def find_and_show():
    db_name = "casco"
    connect(db_name)
    wrong = DataCollection.objects(first_judge_machine=0)[:100]
    for item in wrong:
        draw_wave(item.p)

    plt.show()


if __name__ == '__main__':
    # draw_sin()
    # deal_csv()
    find_and_show()
