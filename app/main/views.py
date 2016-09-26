#!/usr/bin/env python
#coding:utf-8

"""
视图函数
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import render_template,request,session,redirect,url_for,current_app,\
    abort,flash

from ..forms import LawForm
from . import main
from ..models import Law,Platform,Person,Product
from .. import db


#公共函数,转化成utf-8编码
def transformToUTF_8(str):
    if not isinstance(str,'unicode'):
        return unicode(str,'utf-8')
    else:
        return str

@main.route('/',methods=['GET','POST'])
def index():

    form = LawForm()
    if form.validate_on_submit():
        session['title'] = form.title.data
        session['content'] = form.content.data
        return redirect(url_for('main.research'))

    return render_template('index.html',form=form)


@main.route('/research',methods=['GET','POST'])
def research():

    form = LawForm()
    #获取查询参数
    page = request.args.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    title = session['title']
    content = session['content']
    title_encode = unicode('%'+title+'%')
    content_encode = unicode('%'+content+'%')
    obj = Law.query

    #判断查询参数,构建相应查询条件
    if not title and not content:
        pass

    elif title and not content:

        obj = obj.filter(Law.title.like(title_encode))

    elif not title and content:

        obj = obj.filter(Law.content.like(content_encode))

    elif title and content:

        obj = obj.filter(Law.title.like(title_encode)).filter(Law.content.like(content_encode))

    pagination = obj.paginate(page,current_app.config['ARTICLE_PER_PAGE'],False)
    articles = pagination.items

    if articles:
        flash('本页记录%s个'%len(articles))
        return render_template('list.html',articles = articles,pagination = pagination)
    else:

        flash('没有找到相关记录,请调整关键字后查询!')
        return redirect(url_for('main.index',form=form))


@main.route('/article/<string:id>')
def detail(id):

    if id:

        article = Law.query.filter(Law.id == id).first()
        if not article:

            return abort(500)
        else:

            return render_template('detail.html',article = article)
    else:
        return abort(404)

#理财平台列表
@main.route('/platform')
def platform_list():
    pass
    platforms = Platform.query.all()
    return render_template('platform_list.html',platforms=platforms,count=len(platforms))


#平台详情
@main.route('/platform/<string:id>')
def platform(id):

    platform = Platform.query.filter(Platform.id == id).first()
    person = Person.query.filter(Person.platform_id == id).first()
    products = Product.query.filter(Product.platform_id == id).all()
    if platform and person and products:

        return render_template('platform.html',
                               platform = platform,
                               person = person,
                               products = products,
                               )
    else:
        return abort(500)

@main.route('/test')
def test():
    return render_template('test.html')









