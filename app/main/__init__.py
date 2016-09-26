#!/usr/bin/env python
#coding:utf-8

"""
main蓝本
"""

from flask import Blueprint

main = Blueprint('main',__name__)

#此处导入视图及异常处理
from . import views,errors