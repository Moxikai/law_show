#coding:utf-8
from flask import Blueprint

auth = Blueprint('auth',__name__) # 定义auth蓝本名称

from . import views