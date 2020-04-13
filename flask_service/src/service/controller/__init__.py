# -*- coding:utf-8 -*-
"""
File: __init__.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
from flask.blueprints import Blueprint
from flask_restful import Api
from flask_uploads import UploadSet, configure_uploads, ALL

from service.controller import demo_resource
from service.controller import socket_controller
from service.controller import template_controller

from service.manager import file_manager


def register_route(app):
    config_upload(app)
    origin_entry = build_origin_entry()
    auth_entry = build_auth_entry()
    app.register_blueprint(origin_entry, url_prefix="/", name="bp_origin")
    app.register_blueprint(auth_entry, url_prefix="/auth/", name="bp_auth")


def config_upload(app):
    # 文件上传设置
    ac_upload_set = UploadSet(file_manager.upload_mark, ALL)
    app.config[file_manager.upload_dest] = app.default_config.get('data', 'upload_dir')
    configure_uploads(app, ac_upload_set)


def build_origin_entry():
    bp_entry = Blueprint("origin", __name__)
    bp_entry.add_url_rule("/", endpoint='ep_index', view_func=template_controller.demo, methods=['GET'])

    # WebSocket
    bp_entry.add_url_rule("/play/<username>", endpoint='ep_play', view_func=socket_controller.play)
    # 文件上传
    bp_entry.add_url_rule(
        "/upload_file", view_func=template_controller.upload_file, methods=['POST']
    )
    # 文件下载
    bp_entry.add_url_rule(
        "/download_file/<filename>", endpoint='ep_download',
        view_func=template_controller.download_file, methods=['GET']
    )
    # RESTFUL
    rest_api = Api(bp_entry)
    rest_api.add_resource(demo_resource.DemoResource, 'demo_api')

    return bp_entry


def build_auth_entry():
    bp_entry = Blueprint("auth", __name__)
    # bp_entry.add_url_rule("/demo", endpoint='ep_demo', view_func=template_controller.demo2, methods=['GET'])
    # bp_entry.add_url_rule("/login", endpoint='ep_login', view_func=template_controller.login, methods=['GET'])
    # bp_entry.add_url_rule("/user", endpoint='ep_user', view_func=template_controller.user, methods=['GET'])
    # bp_entry.add_url_rule("/user_add", endpoint='ep_user_add', view_func=template_controller.user_add, methods=['GET'])
    # bp_entry.add_url_rule("/password", endpoint='ep_password', view_func=template_controller.password, methods=['GET'])

    # rest_api = Api(bp_entry)
    # rest_api.add_resource(resource_auth.LoginResource, 'login_api')
    # rest_api.add_resource(resource_auth.UserResource, 'user_api')
    # rest_api.add_resource(resource_auth.AuthResource, 'auth_api')

    return bp_entry
