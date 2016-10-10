#!/usr/bin/env python
#coding:utf-8

"""
定义表单
"""

from flask_wtf import Form
from wtforms import StringField,SubmitField,TextAreaField,validators
from wtforms.validators import DataRequired

class LawForm(Form):
    pass
    title = StringField('标题')
    content = StringField('正文')
    submit = SubmitField('查询')

class NewsForm(Form):
    """新闻搜索"""
    keyword = StringField('关键词')
    submit = SubmitField('搜索')

class NewsUpdateForm(Form):
    id = StringField('id',validators=[DataRequired()])
    title = StringField('title',validators=[DataRequired()])
    content = TextAreaField('content',validators=[DataRequired()])
    date_crawl = StringField('date_crawl',validators=[DataRequired()])
    date_publish = StringField('date_publish',validators=[DataRequired()])
    agency_source = StringField('agency_source',validators=[DataRequired()])
    author_source = StringField('author_source',validators=[DataRequired()])
    url_source = StringField('url_source',validators=[DataRequired()])
    url_crawl = StringField('url_crawl',validators=[DataRequired()])
    submit = SubmitField('submit')

