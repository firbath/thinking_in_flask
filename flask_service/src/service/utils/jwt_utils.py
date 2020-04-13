# -*- coding:utf-8 -*-
"""
File: jwt_utils.py
Author: YuFangHui
Date: 2019-05-09
Description:
"""
from datetime import datetime, timedelta

import jwt

from y_utils import time_utils

SECRET_KEY = 'thinking_in_flask'


def token_decode(token):
    if not token:
        return {'code': 2}
    try:
        payload = jwt.decode(token, SECRET_KEY)
        return {'code': 0, 'data': payload}
    except Exception as e:
        return {'code': 1, 'data': str(e)}


def token_encode(user_name, nick_name, role, login_time):
    """生成认证Token"""
    payload = {
        'exp': datetime.utcnow() + timedelta(days=365),
        'iat': datetime.utcnow(),
        'iss': 'thinking_in_flask',

        'user_name': user_name,
        'nick_name': nick_name,
        'role': role,
        'login_time': time_utils.time2str(login_time)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def sys_token_gen():
    """系统专用特殊签名"""
    payload = {
        'exp': datetime.utcnow() + timedelta(days=3650),  # 过期时间
        'iat': datetime.utcnow(),  # 签发时间
        'iss': 'system',  # 签发者

        'user_name': 'system',
        'nick_name': 'system',
        'role': 'administrator',
        'login_time': time_utils.time2str(datetime.now())
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


if __name__ == '__main__':
    usr_token = token_encode('user', 'user', 'user', datetime.now())
    print(usr_token.decode('utf-8'))
    sys_token = sys_token_gen()
    print(sys_token.decode('utf-8'))
