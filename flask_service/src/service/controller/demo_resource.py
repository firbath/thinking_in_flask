# -*- coding:utf-8 -*-
"""
File: video_resource.py
Author: YuFangHui
Date: 2020/2/27
Description:
"""
from flask import request

from service.controller.base_resource import BaseResource
from service.utils import flask_utils
from service.manager import file_manager
from service.manager import demo_manager


class DemoResource(BaseResource):
    f_permission = ''

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'user_check':
            return flask_utils.res_s(action=action, data=self.c_user)
        elif action == 'action_data':
            return flask_utils.res_s(action=action, data=data)
        elif action == 'calculate_24':
            return demo_manager.demo_play(action=action, data=data)
        else:
            return flask_utils.res_f('res no action')

    def get(self):
        return flask_utils.res_s('Hello flask')


class FileResource(BaseResource):
    f_permission = 'USER'

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'list_file':
            rst = file_manager.list_my_file(data.get('user_name'))
            return flask_utils.res_s(action=action, data=rst)
        else:
            return flask_utils.res_f('FileResource no action')

    def get(self):
        return flask_utils.res_s('Hello flask')
