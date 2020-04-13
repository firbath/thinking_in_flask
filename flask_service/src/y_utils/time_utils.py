# -*- coding:utf-8 -*-
"""
File: time_utils.py
Author: YuFangHui
Date: 2019-05-06
Description:
"""
import time
from datetime import datetime

date_fmt = '%Y%m%d%H%M%S'


def get_timestamp():
    t = time.time()
    return int(round(t * 1000))


def time2str(date=None, fmt=date_fmt):
    if not isinstance(date, datetime):
        date = datetime.now()
    return date.strftime(fmt)


def str2time(date_str, fmt=date_fmt):
    return datetime.strptime(date_str, fmt)


def time_delay(date1, date2):
    return (date2 - date1).total_seconds()


def str2time_delay(date_str1, date_str2, fmt=date_fmt):
    return (str2time(date_str2, fmt) - str2time(date_str1, fmt)).total_seconds()


def str2time_ex(date_str, fmt=date_fmt):
    try:
        return datetime.strptime(date_str, fmt)
    except Exception as e:
        print(str(e))
        return None
