#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 18:23
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : atm
# @Software: PyCharm

import os
import sys
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings
from core import main

if __name__ == '__main__':
    main.login()