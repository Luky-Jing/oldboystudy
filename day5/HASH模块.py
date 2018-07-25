#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年2月27日 下午8:29
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : HASH模块.py
# @Software: PyCharm

import hashlib

m = hashlib.md5()
m.update(b'hello')
print(m.hexdigest())