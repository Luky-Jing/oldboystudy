#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 18:23
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : main
# @Software: PyCharm

def login():
    print("Welcome to my atm.")

def run():
    '''
    注释
    :return:
    '''
    acc_data = auth.acc_login(userdata, access_logger)
    if userdata['is_authenticated']:
        user_data['account_data'] = acc_data
        interactive(user_data)