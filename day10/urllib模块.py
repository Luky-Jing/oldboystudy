#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年3月1日 下午2:20
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : urllib模块.py
# @Software: PyCharm

import urllib.request
import urllib.parse


data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf-8')
print(data)
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

import socket
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'Host': 'httpbin.org',
}

dict = {
    'name': 'lipeijing'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

# proxy_handler = urllib.request.ProxyHandler({
#     'http': 'http://www.cnblogs.com',
#     'https': 'https://www.cnblogs.com'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('http://www.cnblogs.com')
# print(response.read())