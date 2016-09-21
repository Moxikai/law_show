#!/usr/bin/env python
#coding:utf-8

"""
配置文件
"""

import os

baseDir = os.path.dirname(__file__)

#基本配置
class Config():
    pass
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

#开发配置,继承至基本配置
class DevelopmentConfig(Config):
    pass
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(baseDir,'data-dev.db')

#生产配置
class ProductionConfig(Config):
    pass
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
        'sqlite:///' + os.path.join(baseDir,'data.db')

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
     'default':DevelopmentConfig,
        }