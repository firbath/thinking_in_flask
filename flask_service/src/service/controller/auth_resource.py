# -*- coding:utf-8 -*-
"""
File: resource_auth.py
Author: YuFangHui
Date: 2019-05-06
Description:
"""
from flask import request

from service.controller.base_resource import BaseResource
from service.manager import user_manager
from service.utils import flask_utils


class AuthResource(BaseResource):
    f_permission = 'USER'

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'user_check':
            return flask_utils.res_s(action=action, data=self.c_user)
        else:
            return flask_utils.res_f('AUTH no action')

    def get(self):
        return flask_utils.res_s('Hello SI AUTH')


class LoginResource(BaseResource):
    f_permission = ''

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'login':
            return user_manager.login_user(action, data)
        else:
            return flask_utils.res_f('AUTH no action')

    def get(self):
        return flask_utils.res_s('Hello SI AUTH')


class UserResource(BaseResource):
    f_permission = 'MANAGER'

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'init_web_data':
            return user_manager.init_web_data(action, self.c_user)
        # elif action == 'register':
        #     return user_manager.register_user(action, data, self.c_user)
        # elif action == 'add_user':
        #     return user_manager.add_user(action, data, self.c_user)
        # elif action == 'del_user':
        #     return user_manager.del_user(action, data, self.c_user)
        # elif action == 'update_user':
        #     return user_manager.update_user(action, data, self.c_user)
        # elif action == 'query_user':
        #     return user_manager.select_user(action, data)
        else:
            return flask_utils.res_f('AUTH no action')

    def get(self):
        return flask_utils.res_s('Hello SI AUTH', data=None)
