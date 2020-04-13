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


class DemoResource(BaseResource):
    si_permission = 'USER'

    def post(self):
        body = request.get_json()
        action = body.get('action')
        data = body.get('data')
        if action == 'user_check':
            return flask_utils.res_s(action=action, data=self.c_user)
        elif action == 'action_data':
            return flask_utils.res_s(action=action, data=data)
        else:
            return flask_utils.res_f('res no action')

    def get(self):
        return flask_utils.res_s('Hello flask')
