# -*- coding:utf-8 -*-
"""
File: manager.py
Author: YuFangHui
Date: 2019-07-08
Description:
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_service import app
from service.module.database import mysql_db

manager = Manager(app)
# 1. 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, mysql_db)
# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
