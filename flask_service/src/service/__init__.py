# -*- coding:utf-8 -*-
"""
File: __init__.py
Author: YuFangHui
Date: 2020/3/2
Description:
"""

from flask import Flask
from flask_cors import CORS

from service.controller import register_route
from service.manager import register_manager
from service.module import register_module
from service.module.config import get_config


def create_app():
    app = Flask(
        __name__,
        static_folder='../../static',
        template_folder='../../templates',
        static_url_path='/y'
    )
    # 跨域支持
    CORS(app, supports_credentials=True)
    # 注册组件
    register_module(app)
    # 注册功能
    register_manager(app)
    # 注册路由
    register_route(app)

    # 全局前缀
    url_prefix = get_config().get('config', 'context')
    if url_prefix:
        from werkzeug.middleware.dispatcher import DispatcherMiddleware

        def simple(env, resp):
            resp('200 OK', [('Content-Type', 'text/plain')])
            return [b'Hello WSGI World']

        app.wsgi_app = DispatcherMiddleware(simple, {url_prefix: app.wsgi_app})

    return app
