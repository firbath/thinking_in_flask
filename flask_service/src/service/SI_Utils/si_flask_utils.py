# -*- coding:utf-8 -*-
"""
File: si_flask_utils.py
Author: YuFangHui
Date: 2019-05-06
Description:
"""
from functools import wraps

from flask import current_app
from flask import jsonify
from flask import request
from flask_restful import Resource
from service.SI_Utils import time_utils
from service.SI_Utils import si_token_utils
from datetime import datetime as p_datetime  # 有时候会返回datatime类型
from datetime import date, time
from sqlalchemy import DateTime, Numeric, String, Date, Time  # 有时又是DateTime


def show_all_route(app):
    print('~~~~~show_all_route~~~~~')

    if not app:
        print('no app')
        print('~~~~~~~~~~~~~~~~~~~~~~~~')
        return

    if not app.view_functions:
        print('no app.view_functions')
    else:
        for key, func in app.view_functions.items():
            print(key, func)
    print('~~~~~~~~~~~~~~~~~~~~~~~~')

    if not app.url_map:
        print('no app.url_map')
    else:
        print(app.url_map)
    print('~~~~~~~~~~~~~~~~~~~~~~~~')


def res_s(msg='request success', action=None, data=None):
    return res(True, msg, action, data)


def res_f(msg='request failed', action=None, data=None):
    return res(False, msg, action, data)


def res(success=True, msg='si_response', action=None, data=None):
    return jsonify({
        'success': success,
        'time': time_utils.time2str(),
        'msg': msg,
        'action': action,
        'data': data
    })


def base_token_check(func, permission_check):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        functools.wraps 则可以将原函数对象的指定属性复制给包装函数对象, 默认有 __module__、__name__、__doc__,或者通过参数选择
        """
        token = request.headers.get("access-token")
        rst = si_token_utils.token_decode(token)
        if rst.get('code') == 0:
            # 用户鉴权
            payload = rst.get('data')
            if permission_check(payload):
                return func(*args, **kwargs)
            else:
                return res_f(msg='permission denied', action='permission_error')
        elif rst.get('code') == 1:
            current_app.app_logger.error('token_required:{}'.format(rst.get('data')))
            return res_f(msg='token is invalid:{}'.format(rst.get('data')), action='token_error')
        else:
            return res_f(msg='token is invalid', action='token_error')

    return wrapper


def get_user():
    token = request.headers.get("access-token")
    rst = si_token_utils.token_decode(token)
    if rst.get('code') == 0:
        payload = rst.get('data')
        if payload:
            return {
                'user_name': payload.get('si_name'),
                'nick_name': payload.get('si_nick'),
                'role': payload.get('si_role'),
                'login_time': payload.get('si_time')
            }
    return None


def model_to_dict(model):
    m_dict = dict()
    for col in model.__table__.columns:
        if isinstance(col.type, DateTime):
            value = time_utils.time2str(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        # yield (col.name, value)
        m_dict[col.name] = value
    return m_dict


def fill_model_by_dict(model, m_dict):
    for col in model.__table__.columns:
        value = m_dict.get(col.name)
        if not value:
            continue
        if isinstance(col.type, DateTime):
            value = time_utils.str2time(value)
        elif isinstance(col.type, Numeric):
            value = float(value)
        setattr(model, col.name, value)
    return model


def filter_str_by_dict(model, m_dict, filters, match=False):
    for col in model.__table__.columns:
        value = m_dict.get(col.name)
        if value and isinstance(col.type, String):
            if match:
                filters += (col == value.strip(),)
            else:
                filters += (col.contains(value.strip()),)
            # filters += (AccountInfo.id > 1,)
    return filters


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def find_datetime(value):
    for v in value:
        if isinstance(value[v], p_datetime):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:

        if isinstance(value, (p_datetime, DateTime)):
            return time_utils.time2str(value)
        elif isinstance(value, (date, Date)):
            # return value.strftime("%Y-%m-%d")
            return time_utils.time2str(value)
        elif isinstance(value, (Time, time)):
            # return value.strftime("%H:%M:%S")
            return time_utils.time2str(value)
    else:
        return ""


class SiResource(Resource):
    si_permission = ''

    def __init__(self):
        # 通过method_decorators管理注解,实现对所用方法的权限约束
        # 通过token实现user-role-permission权限管理
        # si_permission为空,无须校验,不添加权限注解
        if self.__class__.si_permission and self.__class__.token_check not in self.__class__.method_decorators:
            self.__class__.method_decorators = self.__class__.method_decorators + [self.__class__.token_check]
            print(self.__class__.method_decorators)

    @classmethod
    def permission_check(cls, payload):
        print('SiResource permission_check', cls.__name__)
        print('payload', payload)
        return False

    @classmethod
    def token_check(cls, func):
        # print cls.__name__, cls.method_decorators
        return base_token_check(func=func, permission_check=cls.permission_check)
