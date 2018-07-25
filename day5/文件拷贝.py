#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年2月26日 下午3:26
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : 文件拷贝.py
# @Software: PyCharm

import shutil
import os

shutil.copyfile("file1", "file2")

print(os.stat("file1"))
