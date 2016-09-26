#!/usr/bin/env python
#coding:utf-8

"""
定义表单
"""

from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class LawForm(Form):
    pass
    title = StringField('标题')
    content = StringField('正文')
    submit = SubmitField('查询')
