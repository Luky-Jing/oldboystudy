#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 22:33
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : module_test
# @Software: PyCharm

import random

checkcode = ''

for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        tmp = chr(random.randrange(65, 90))
    else:
        tmp = random.randint(0, 9)
    checkcode += str(tmp)

print(checkcode)