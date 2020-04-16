# -*- coding:utf-8 -*-
"""
File: user_manager.py
Author: YuFangHui
Date: 2019-05-09
Description:
"""

import json
import os
from datetime import datetime

from service.module import param
from service.module import config
from service.utils import flask_utils
from service.utils import jwt_utils


def login_user(action, data):
    """
    用户登录
    """
    rst = find_user(data)
    code = rst.get('code')
    if code == 0:
        success = True
        message = '用户登录成功'
    elif code == 1:
        success = False
        message = '用户名和密码不能为空'
    elif code == 2:
        success = False
        message = '用户不存在'
    elif code == 3:
        success = False
        message = '密码错误'
    else:
        success = False
        message = '用户注册失败'
    return flask_utils.res(success, message, action, rst.get('data'))


def init_web_data(action, c_user):
    data = {
        'user': c_user,
        'role_list': [] + param.get_all_role_list()
    }
    success = True
    message = '查询成功'
    return flask_utils.res(success, message, action, data)


def init_admin_data(action, c_user):
    data = {
        'user': c_user,
        'all_roles': ','.join(param.get_all_role_list())
    }
    success = True
    message = '查询成功'
    return flask_utils.res(success, message, action, data)


def find_user(data):
    """
    用户登录
    """
    username = data.get('user_name')
    password = data.get('password')
    if not username or not password:
        return {'code': 1}

    users = dict()
    try:
        with open(os.path.join(config.get_param_dir(), 'users.json'), 'r') as f:
            users = json.load(f)
    except Exception as e:
        print(e)

    user = users.get(username)
    if not user:
        return {'code': 2}
    if not user.get("pwd") == password:
        return {'code': 3}

    login_time = datetime.now()

    token = jwt_utils.token_encode(user.get("usr"), user.get("usr"), user.get("role"), login_time)
    return {'code': 0, 'data': {'token': token.decode("utf-8")}}
