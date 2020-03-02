# -*- coding:utf-8 -*-
"""
File: FileManager.py
Author: YuFangHui
Date: 2020/2/28
Description:
"""
import os
import requests

from flask import current_app


def init_work_dir(date):
    work_dir = os.path.join(current_app.default_config.get('data', 'work_dir'), date)
    if check_dir(work_dir, True):
        return work_dir
    return None


def check_dir(dir_path, flag=True):
    if os.path.isdir(dir_path):
        return True
    elif flag:
        os.makedirs(dir_path)
    return os.path.isdir(dir_path)


def download_file(url, path):
    dir_path, file_name = os.path.split(path)
    if check_dir(dir_path):
        r = requests.get(url)
        with open(path, "wb") as code:
            code.write(r.content)
    return os.path.exists(path)
