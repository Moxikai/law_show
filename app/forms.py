#!/usr/bin/env python
#coding:utf-8

"""
定义表单
"""

from flask_wtf import Form
from wtforms import StringField,SubmitField,TextAreaField,validators,RadioField
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

class CaseForm(Form):
    """案例表单"""
    title = StringField('标题',validators=[DataRequired()])
    date = StringField('时间',validators=[DataRequired()])
    location = StringField('地区',validators=[DataRequired()])
    persons_involved = StringField('涉案人员',validators=[DataRequired()])
    company_involved = StringField('公司信息',validators=[DataRequired()])
    means_description = TextAreaField('诈骗手段',validators=[DataRequired()])
    victims = StringField('受害人',validators=[DataRequired()])
    momeny_involved = StringField('涉案金额',validators=[DataRequired()])
    agency = StringField('执法机关',validators=[DataRequired()])
    courts = StringField('宣判法院',validators=[DataRequired()])
    sentence = TextAreaField('判决结果',validators=[DataRequired()])
    keywords = TextAreaField('关键词',validators=[DataRequired()])
    submit = SubmitField('提交')

class DocumentUpdateForm(Form):
    """更新文书表单"""
    title = StringField('标题',)
    types = StringField('类型',)
    court = StringField('审理法院',)
    document_code = StringField('文书号')
    document_type = StringField('文书类型')
    conclusion_date = StringField('审结日期')
    proceeding = StringField('审理程序')
    judgment = TextAreaField('审判结果')
    area_first = StringField('省')
    area_second = StringField('市')
    url = StringField('链接')
    submit = SubmitField('submit')

class DocumentsSearchForm(Form):
    """通用搜索表单"""
    type = StringField('类型') # 搜索类型
    keywords = StringField('全文',validators=[DataRequired()]) # 搜索内容
    submit = SubmitField('submit') # 提交




