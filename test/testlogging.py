#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18年2月6日 上午10:54
# @Author  : lipeijing
# @Email   : lipeijing@jd.com
# @File    : testlogging.py
# @Software: PyCharm

import os
import logging

def init_logger():
    log_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/log/"
    #log_dir = os.path.dirname(__file__)[:-4] + "/log/"
    log_level = logging.DEBUG
    logger_name_list = ['MonitorNetworkLog','MoniorNpApiLog']
    for logger_name in logger_name_list:
        log_filename = log_dir + logger_name + ".log"
        #不存在日志目录就创建目录
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        #不存在日志文件就创建日志文件
        if not os.path.isfile(log_filename):
            fobj = open(log_filename,'w')
            fobj.close()
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        formatter_general = logging.Formatter("%(asctime)s - "\
                             + " " + "[%(levelname)s] - "\
                             + "[%(funcName)s:%(lineno)d] - %(message)s")
        handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=1000000000, backupCount=2)
        handler.setFormatter(formatter_general)
        logger.addHandler(handler)

if __name__ == "__main__":
    init_logger()