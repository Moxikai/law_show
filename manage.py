#!/usr/bin/env python
#coding:utf-8

"""
启动脚本
"""

import os

from app import create_app,db
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand
from app.models import Law

app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app,db)

#注册shell命令
def make_shell_context():
    pass
    return dict(app=app,db=db,Law=Law)

manager.add_command('shell',Shell(make_context=make_shell_context()))
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    pass
    manager.run()
