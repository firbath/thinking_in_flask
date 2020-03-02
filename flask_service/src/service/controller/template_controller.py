# -*- coding:utf-8 -*-
"""
File: template_controller.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
from flask import make_response
from flask import render_template, request
from flask import send_from_directory

from service.files import file_manager
from service.module import config
from service.SI_Utils import si_flask_utils
from service.SI_Utils import si_token_utils


def demo():
    # return 'Hello World'
    return render_template('demo.html')


def upload_file():
    up_list = list()
    user_name = None
    token = request.headers.get("access-token")
    rst = si_token_utils.token_decode(token)
    if rst.get('code') == 0:
        try:
            user_name = rst.get('data').get('si_name')
        except Exception as e:
            print(e)
        # # 用户鉴权
        # payload = rst.get('data')
        # c_user = {
        #     'user_name': payload.get('si_name'),
        #     'nick_name': payload.get('si_nick'),
        #     'role': payload.get('si_role'),
        #     'login_time': payload.get('si_time')
        # }
    if user_name and request.method == 'POST' and 'media' in request.files:
        file_list = request.files.getlist('media')
        up_list = file_manager.upload_files(file_list, user_name)
    if up_list:
        return si_flask_utils.res_s(action='upload_file', data=up_list)
    return si_flask_utils.res_f(action='upload_file')


def download_file(filename):
    # 需要知道2个参数, 第1个参数是本地目录的path, 第2个参数是文件名(带扩展名)
    response = make_response(send_from_directory(config.get_download_dir(), filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
    return response
