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

class CaseForm(Form):
    """案例表单"""
    title = StringField('标题',validators=[DataRequired()])
    date_start = StringField('起始时间',validators=[DataRequired()]) # 起始日期
    date_end = StringField('截止时间', validators=[DataRequired()]) # 截止日期
    province = StringField('省',validators=[DataRequired()]) # 省
    city = StringField('市',validators=[DataRequired()]) # 市
    county = StringField('区县',validators=[DataRequired()]) # 区县
    persons_involved = StringField('涉案人员',validators=[DataRequired()]) # 涉案人员
    company_involved = StringField('公司信息',validators=[DataRequired()])
    means_description = TextAreaField('诈骗手段',validators=[DataRequired()])
    victims = StringField('受害人',validators=[DataRequired()])
    momeny_involved = StringField('涉案金额',validators=[DataRequired()])
    agency = StringField('执法机关',validators=[DataRequired()])
    courts = StringField('宣判法院',validators=[DataRequired()])
    sentence = TextAreaField('判决结果',validators=[DataRequired()])
    keywords = TextAreaField('关键词',validators=[DataRequired()])
    #submit = SubmitField('提交')

class AreaUpdateForm(Form):
    """更新到区县行政区划"""
    code = StringField('行政区划代码',validators=[DataRequired()])
    area_name = StringField('地区名称',validators=[DataRequired()])
    level = StringField('层级',validators=[DataRequired()])
    code_highlevel = StringField('上级代码')
    submit = SubmitField('submit')

class UpdateDocumentForm(Form):
    """更新判决文书"""
    id = StringField('id',validators=[DataRequired()])
    url = StringField('url')
    title = StringField('title')
    location = StringField('location')
    types = StringField('types')
    court = StringField('court')
    document_code = StringField('document_code')
    document_type = StringField('document_type')
    conclusion_date = StringField('conclusion_date')
    proceeding = StringField('proceeding')
    trial_person = StringField('trial_person')
    judgment = StringField('judgment')
    submit = SubmitField('submit')

