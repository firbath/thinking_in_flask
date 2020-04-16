# -*- coding:utf-8 -*-
"""
File: base_resource.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
import json
import os

from flask import current_app

from service.utils import flask_utils
from service.module import config


class BaseResource(flask_utils.FlaskResource):
    c_user = None
    f_permission = ''

    def __init__(self):
        flask_utils.FlaskResource.__init__(self)
        # print self.__class__.__name__, self.__class__.res_level

    @classmethod
    def permission_check(cls, payload):
        if payload:
            f_role = payload.get('role')

            # 解析用户
            cls.c_user = {
                'user_name': payload.get('user_name'),
                'nick_name': payload.get('nick_name'),
                'role': f_role,
                'login_time': payload.get('login_time')
            }

            # 系统指令,跳过权限
            if payload.get('iss') == 'system':
                current_app.app_logger.warning('system request')
                return True

            # 校验权限
            path = os.path.join(config.get_param_dir(), 'role_permission.json')
            permissions = list()
            try:
                with open(path, 'r') as f:
                    permissions = permissions + json.load(f).get(f_role)
            except Exception as e:
                print(e)
            return cls.f_permission in permissions

        return False
