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


class BaseResource(flask_utils.SiResource):
    c_user = None
    si_permission = ''

    def __init__(self):
        flask_utils.SiResource.__init__(self)
        # print self.__class__.__name__, self.__class__.res_level

    @classmethod
    def permission_check(cls, payload):
        if payload:
            si_role = payload.get('si_role')

            # 解析用户
            cls.c_user = {
                'user_name': payload.get('si_name'),
                'nick_name': payload.get('si_nick'),
                'role': si_role,
                'login_time': payload.get('si_time')
            }

            # 系统指令,跳过权限
            if payload.get('iss') == 'si_system':
                current_app.app_logger.warning('si_system request')
                return True

            # 校验权限
            path = os.path.join(config.get_param_dir(), 'role_permission.json')
            permissions = list()
            try:
                with open(path, 'r') as f:
                    permissions = permissions + json.load(f).get(si_role)
            except Exception as e:
                print(e)
            return cls.si_permission in permissions

        return False
