# -*- coding:utf-8 -*-
"""
File: database.py
Author: YuFangHui
Date: 2019-05-07
Description:
"""
from flask_sqlalchemy import SQLAlchemy

mysql_db = SQLAlchemy()


def init_app(app):
    # 配置
    config = app.default_config
    # 数据库
    db_info = config.get('data', 'sqlite')
    db_uri = 'sqlite:///%s?charset=utf8' % db_info
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 80
    # 数据库初始化
    mysql_db.init_app(app)
