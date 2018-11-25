# -*- coding:utf-8 -*-
from flask_script import Manager, Server
from web_app import app
from web_app.models import db, User

manager = Manager(app)
manager.add_command('server', Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


if __name__ == '__main__':
    manager.run()
