#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : json序列化
# @Software: PyCharm
import json
import pickle

def sayhi(name):
    print('hello, ', name)
info = {
    'name': 'lipeijing',
    'age': 22,
    'func': sayhi
}

# f = open("test.txt", "w")
# # print(json.dumps(info))
# f.write(json.dumps(info))

f = open("test.txt", "r")
date = json.loads(f.read())

f.close()

print(date['age'])

