#!/usr/bin/env python
#coding:utf-8

"""

"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
# 保护级别设为strong,记录ip和代理信息,发现异常登出
login_manager.session_protection = 'strong'
# 设置登录视图
login_manager.login_view = 'auth.login'

def create_app(config_name):
    pass
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    #此处注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')


    return app

