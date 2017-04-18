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
    id_num = IntField()
    facility_type = IntField()
    direction = IntField()
    p = ListField()
    a = ListField()
    b = ListField()
    c = ListField()
    is_man_made = IntField()
    first_judge_machine = IntField()
    first_judge_artificial = IntField()
    second_judge_machine = IntField()
    second_judge_artificial = IntField()


class DataCollectionClass:
    def __init__(self):
        self.db_name = "casco"
        connect(self.db_name)

    @staticmethod
    def insert(id, p, a, b, c, f, d, man, f1, f2, s1, s2):
        DataCollection(
            id_num=id,
            facility_type=f,
            direction=d,
            p=p,
            a=a,
            b=b,
            c=c,
            is_man_made=man,
            first_judge_machine=f1,
            first_judge_artificial=f2,
            second_judge_machine=s1,
            second_judge_artificial=s2
        ).save()


def deal_csv():
    file = 'casco_train.csv'
    total = pd.read_csv(file)
    for i in range(190642):
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
        f = total['facility_type'][i]
        d = int(total['direction'][i])
        f1 = total['first_judge_machine'][i]
        f2 = total['first_judge_artificial'][i]
        s1 = total['second_judge_machine'][i]
        s2 = total['second_judge_artificial'][i]
        bsbsbs = DataCollectionClass()
        bsbsbs.insert(p, a, b, c, f, d, man, f1, f2, s1, s2)


def draw_sin():
    s = [1, 2, 3]
    t = np.array(s)
    y = np.array(s)
    z = np.cos(2 * np.pi * t / 256)
    plt.plot(t, y, 'black')
    plt.show()
    plt.plot(t, z, 'red')
    plt.show()


def draw_wave(switch_data, right=True):
    if right:
        color = 'black'
    else:
        color = 'red'
    t = np.arange(0, 10, 0.01)
    data = switch_data
    plt.plot(t, data, color)


def find_and_show():
    db_name = "casco"
    connect(db_name)
    right = DataCollection.objects(first_judge_machine=0)[:50]
    for item in right:
        draw_wave(item.p)
    wrong = DataCollection.objects(first_judge_machine=1)[:30]
    for item in wrong:
        draw_wave(item.p, False)

    plt.show()


if __name__ == '__main__':
    # draw_sin()
    # deal_csv()
    find_and_show()
