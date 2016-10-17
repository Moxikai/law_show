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
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASKY_MAIL_SUBJECT_PREFIX = '菲凡新用户' # 邮件主题前缀
    FLASKY_MAIL_SENDER = 'FeiFandata<threeangel@qq.com>'
    FLASKY_ADMIN = 'new_flasky@qq.com'


#开发配置,继承至基本配置
class DevelopmentConfig(Config):
    pass
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///'+os.path.join(baseDir,'data-dev.db')
    ARTICLE_PER_PAGE = 12
    NEWS_PER_PAGE = 10
    # 邮件服务器设置
    MAIL_SERVER = 'smtp.qq.com' # smtp服务器地址
    MAIL_PORT = 465 # 邮件服务器端口
    MAIL_USE_TLS = False # 是否启用tls
    MAIL_USE_SSL = True # 使用SSL
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # 发送人邮箱用户名
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') # 发送人邮箱密码

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