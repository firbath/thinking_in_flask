# -*- coding:utf-8 -*-
from os import path


class Config(object):
    # 缺省情况下,采用sqlite作为基础数据库
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + path.join(path.pardir, '/database.db')


class ProdConfig(Config):
    # 生产环境,使用mysql示例
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip:port/db_name'
    pass


class DevConfig(Config):
    DEBUG = True
