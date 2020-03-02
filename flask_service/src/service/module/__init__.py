# -*- coding:utf-8 -*-
"""
File: __init__.py
Author: YuFangHui
Date: 2019/11/19
Description:
"""
from service.module import config
from service.module import database
from service.module import logger


def register_module(app):
    config.init_app(app)
    logger.init_app(app)
    database.init_app(app)
