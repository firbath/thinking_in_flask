'''
Author: FirbathYu firbath@163.com
Date: 2023-02-16 16:03:38
LastEditors: FirbathYu firbath@163.com
LastEditTime: 2023-02-16 17:15:28
Description: 
'''
# -*- coding:utf-8 -*-
import json
import os
from datetime import datetime

from service.module import param
from service.module import config
from service.utils import flask_utils
from service.utils import jwt_utils

from demo import points


def demo_play(action, data):
    nums = data.get('nums')
    num_list_src = nums.split(" ")
    # test_itertools("1 2 3 4", 2)
    steps = list()
    rstList = points.playGame(num_list_src)
    if len(rstList) > 0:
        for rst in rstList:
            steps.append(rst.get("step"))
        success = True
        message = 'complate'
    else:
        success = True
        message = 'not find'
    return flask_utils.res(success, message, action, steps)
