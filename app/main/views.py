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

from ..forms import LawForm,NewsForm,NewsUpdateForm,CaseForm,DocumentUpdateForm,DocumentsSearchForm
from . import main
from ..models import Law,Platform,Product,Company,News,Case,Document

from ..forms import LawForm,NewsForm,NewsUpdateForm,CaseForm,AreaUpdateForm
from . import main
from ..models import Law,Platform,Product,Company,News,Case,Area
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
    #监测是否存在多关键字
    #title_encode = unicode('%'+title+'%')
    #content_encode = unicode('%'+content+'%')
    obj = Law.query
    #判断查询参数,构建相应查询条件
    if not title and not content:
        pass
    elif title and not content:
        #以空格分隔
        titles = title.split(' ')
        for title in titles:
            title_encode = unicode('%'+title+'%')
            obj = obj.filter(Law.title.like(title_encode))

    elif not title and content:
        contents = content.split(' ')
        for content in contents:
            content_encode = unicode('%'+content+'%')
            obj = obj.filter(Law.content.like(content_encode))

    elif title and content:
        titles = title.split(' ')
        contents = content.split(' ')
        for title in titles:
            title_encode = unicode('%'+title+'%')
            for content in contents:
                content_encode = unicode('%' + content + '%')
                obj = obj.filter(Law.title.like(title_encode)).filter(Law.content.like(content_encode))

    obj = obj.order_by(Law.effectDate.desc())

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

    platforms = Platform.query.order_by(Platform.gradeFromThird.asc()).all()
    #获取公司信息列表
    companys = Company.query.all()
    id_list = [company.platform_id for company in companys]
    count = 0
    for platform in platforms:
        if platform.id in id_list:
            count += 1
    flash('当前平台数量%s个，目前已更新公司信息(绿色标记)数量%s个'%(len(platforms),count))
    return render_template('platform_list.html',platforms=platforms,id_list = id_list,count=len(platforms))


#平台详情
@main.route('/platform/<string:id>')
def platform(id):

    platform = Platform.query.filter(Platform.id == id).first()
    products = Product.query.filter(Product.platform_id == id).all()
    #if platform and person and products:
    company = Company.query.filter(Company.platform_id == id).first()
    return render_template('platform.html',
                           platform = platform,
                           products = products,
                           company = company,
                           url = 'http://%s'%(platform.url),
                           )
    #else:
        #return abort(500)

@main.route('/test')
def test():
    return render_template('test.html')

@main.route('/news',methods=["GET","POST"])
def news():
    """新闻资讯首页"""
    form = NewsForm() # 实例化表单
    if form.validate_on_submit():
        """接收post数据"""
        keywords = form.keyword.data
        return redirect(url_for('main.news',keywords=keywords,page=1))

    #获取页码
    page = request.args.get('page')
    if not page:
        page = 1 # 默认第一页
    else:
        page = int(page) # 转换成数字
    #获取查询关键词
    keywords = request.args.get('keywords')
    if not keywords:
        """关键词为空"""
        pagination = News.query.order_by(News.date_publish.desc()).paginate(page,current_app.config['NEWS_PER_PAGE'],False)

    else:
        """关键词不为空"""
        #提取关键词
        keyword_list = keywords.split(' ')
        obj = News.query # 初始查询
        for keyword in keyword_list:
            if keyword:
                keyword = unicode('%'+keyword+'%')
                obj = obj.filter(News.content.like(keyword))
        obj = obj.order_by(News.date_publish.desc()) # 按照发布时间降序排列
        pagination = obj.paginate(page,current_app.config['NEWS_PER_PAGE'],False)

    news_list = pagination.items

    if news_list:
        return render_template('news_list.html', news_list=news_list, pagination=pagination,form=form)
    else:
        flash('没有搜索到新闻资讯，请减少关键词重新搜索')
        return render_template('news_list.html', news_list=news_list, pagination=pagination, form=form)

@main.route('/news/<string:id>')
def news_detail(id):
    """资讯详情"""
    news = News.query.get_or_404(id)
    return render_template('news_detail.html',news=news)


@main.route('/news/update',methods=['GET','POST'])
def updateNews():
    """更新新闻数据，api上线前作为过渡方案"""
    form = NewsUpdateForm()
    if request.method == 'POST':
        pass
        print '收到post请求'
        news = News(id = request.form['id'],
                    title = request.form['title'],
                    content = request.form['content'],
                    date_publish = request.form['date_publish'],
                    date_crawl = request.form['date_crawl'],
                    agency_source = request.form['agency_source'],
                    author_source = request.form['author_source'],
                    url_source = request.form['url_source'],
                    url_crawl = request.form['url_crawl']
                    )
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('main.news'))

    return render_template('update_news.html',form=form)

@main.route('/news/delete/<string:id>')
def deleteNews(id):
    """删除新闻记录"""
    news = News.query.get_or_404(id)
    db.session.delete(news)
    flash('新闻记录已删除成功')
    return redirect(url_for('main.news'))

@main.route('/news/handle/<string:id>',methods=["GET","POST"])
def news_handle(id):
    """案例整理"""
    form = CaseForm()
    news = News.query.get_or_404(id)
    if request.method == 'POST':
        print '检测到post数据'
        case = Case(title = request.form['title'],
                    date = request.form['date'],
                    location = request.form['location'],
                    persons_involved = request.form['persons_involved'],
                    company_involved = request.form['company_involved'],
                    means_description = request.form['means_description'],
                    victims = request.form['victims'],
                    momeny_involved = request.form['momeny_involved'],
                    agency = request.form['agency'],
                    courts = request.form['courts'],
                    sentence = request.form['sentence'],
                    keyword = request.form['keywords'],
                    news_id = id)
        db.session.add(case)
        db.session.commit()
        flash('案例已提交！')
        return redirect(url_for('main.news_handle',id=id))
    # 是否有对应整理的案例
    case = Case.query.filter_by(news_id=id).first()
    if case:
        form.title.data = case.title
        form.date.data = case.date
        form.location.data = case.location
        form.persons_involved.data = case.persons_involved
        form.company_involved.data = case.company_involved
        form.means_description.data = case.means_description
        form.victims.data = case.victims
        form.momeny_involved.data = case.momeny_involved
        form.agency.data = case.agency
        form.courts.data = case.courts
        form.sentence.data = case.sentence
        form.keywords.data = case.keyword
    return render_template('news_handle.html',form=form,news=news)

@main.route('/document/update',methods=['GET','POST'])
def documentUpdate():
    """更新文书接口"""
    form = DocumentUpdateForm()
    if request.method == 'POST':

        document = Document(title=request.form['title'],
                            types=request.form['types'],
                            court=request.form['court'],
                            document_code=request.form['document_code'],
                            document_type=request.form['document_type'],
                            conclusion_date=request.form['conclusion_date'],
                            proceeding=request.form['proceeding'],
                            judgment=request.form['judgment'],
                            area_first=request.form['area_first'],
                            area_second=request.form['area_second'],
                            url=request.form['url'],
                            )
        db.session.add(document)
        db.session.commit()
        return '<h1>SUCCESS</h1>',200


    return render_template('document_update.html',form=form)


@main.route('/document',methods=['GET','POST'])
def document_index():
    """文书展示，查询视图"""
    form = DocumentsSearchForm() # 实例化表单

    if form.validate_on_submit():
        """处理post数据"""
        type = form.type.data
        keywords = form.keywords.data
        return redirect(url_for('main.document_index',page=1,type=type,keywords=keywords))

    """处理查询参数"""
    page = request.args.get('page') # 页码
    if page:
        page = int(page)
    else:
        page = 1  # 默认第一页
    type = request.args.get('type') # 查询类型
    if not type:
        type = 'title'  # 默认全文搜索
    keywords = request.args.get('keywords') # 查询关键词
    if keywords:
        keyword_list = keywords.split(' ')
        keyword_list = [keyword for keyword in keyword_list if keyword]  # 去除空白元素
    else:
        keyword_list = [] # 默认空白
    """处理数据查询"""
    obj = Document.query # 初始查询
    if keyword_list:
        for keyword in keyword_list:
            keyword = unicode('%' + keyword + '%')
            if type == 'title':
                obj = obj.filter(Document.title.like(keyword))
            elif type == 'full_content':
                obj = obj.filter(Document.judgment.like(keyword))
    # 计算查询结果数量
    count = obj.count()
    # 排序操作、分页,默认按照审结日期降序排列
    pagination = obj.order_by(Document.conclusion_date.desc()).\
        paginate(page,current_app.config['DOCUMENTS_PER_PAGE'],False)
    document_list = pagination.items
    return render_template('document_index.html',form=form,pagination=pagination,count=count,document_list=document_list)

@main.route('/document/<int:id>')
def document_detail(id):
    """文书详情"""
    document = Document.query.get_or_404(id)
    return render_template('document_detail.html',document=document)









@main.route('/area/update',methods=['GET','POST'])
def updateArea():
    """更新行政区划"""
    form = AreaUpdateForm()
    if request.method == 'POST':
        print '收到post请求'
        area = Area(code = request.form['code'],
                    area_name = request.form['area_name'],
                    level = int(request.form['level']),
                    code_highlevel = request.form['code_highlevel'],
                    )
        try:
            db.session.add(area)
            db.session.commit()
            flash('行政区划已更新')
        except Exception as e:
            print '当前出错:',area.area_name,area.code,'\n',e
            area_check = Area.query.filter_by(code=area.code).first()
            if area_check:
                print '以上记录存在,重复导致错误'
            else:
                print '以上记录并不存在,请检查错误原因'
        return redirect(url_for('main.updateArea'))

    return render_template('area_update.html',form=form)










