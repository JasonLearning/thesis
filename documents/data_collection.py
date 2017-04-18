#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 下午1:17
# @Author  : Aries
# @File    : data_collection.py

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
