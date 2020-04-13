# -*- coding:utf-8 -*-
"""
File: config.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
import os

import configparser

from y_utils import tools


def get_config():
    config = configparser.ConfigParser()
    # path = os.path.split(os.path.realpath(__file__))[0] + '/../../../config_prd.ini'
    path = os.path.split(os.path.realpath(__file__))[0] + '/../../../config_dev.ini'
    config.read(path, encoding='utf-8')
    return config


def get_download_dir():
    dir_path = get_config().get('data', 'download_dir')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def get_param_dir():
    dir_path = os.path.split(os.path.realpath(__file__))[0] + '/../../../param'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def get_dh_dir():
    dir_path = os.path.split(os.path.realpath(__file__))[0] + '/../../../dh'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path


def get_version():
    path = os.path.split(os.path.realpath(__file__))[0] + '/../../../ver.txt'
    ver = tools.read_file(path)
    return ver


def init_app(app):
    app.default_config = get_config()
