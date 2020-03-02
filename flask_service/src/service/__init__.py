# -*- coding:utf-8 -*-
"""
File: __init__.py
Author: YuFangHui
Date: 2020/3/2
Description:
"""

from flask import Flask
from flask_cors import CORS

from service.SI_Utils import time_utils
from service.controller import register_route
from service.manager import register_manager
from service.module import register_module


def create_app():
    app = Flask(__name__, static_folder='../../static', template_folder='../../templates')
    # 跨域支持
    CORS(app, supports_credentials=True)
    # 注册组件
    register_module(app)
    # 注册功能
    register_manager(app)
    # 注册路由
    register_route(app)

    return app
