#coding:utf-8
from flask import Blueprint
api = Blueprint('api',__name__)

# 此处导入视图
from . import errors,document