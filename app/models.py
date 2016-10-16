#!/usr/bin/env python
#coding:utf-8

"""
模型
"""


from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,url_for
from . import db
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    """加载用户的回调函数

    """
    return User.query.get(int(user_id))


class Law(db.Model):
    __tablename__ = 'law'

    id = db.Column(db.String(48),primary_key=True)
    title = db.Column(db.String(48))
    type = db.Column(db.String(48))
    publishDepartment = db.Column(db.String(48))
    publishDate = db.Column(db.String(48))
    effectDate = db.Column(db.String(48))
    loseEffectDate = db.Column(db.String(48))
    status = db.Column(db.String(48))
    content = db.Column(db.Text)

class Platform(db.Model):
    __tablename__ = 'platform'

    id = db.Column(db.String(48),primary_key=True)
    name = db.Column(db.String(48))
    gradeFromThird = db.Column(db.String(48))
    profitAverage = db.Column(db.String(48))
    dateSale = db.Column(db.String(48))
    registeredCapital = db.Column(db.String(48))
    area = db.Column(db.String(48))
    url = db.Column(db.String(48))
    startMoney = db.Column(db.String(48))
    managementFee = db.Column(db.String(48))
    cashTakingFee = db.Column(db.String(48))
    backGround = db.Column(db.String(48))
    provisionOfRisk = db.Column(db.String(48))
    foundCustodian = db.Column(db.String(48))
    safeguardWay = db.Column(db.String(48))
    assignmentOfDebt = db.Column(db.String(48))
    automaticBidding = db.Column(db.String(48))
    cashTime = db.Column(db.String(48))
    abstract = db.Column(db.Text)
    manageTeam = db.Column(db.Text)
    products = db.relationship('Product',backref='platform')
    companys = db.relationship('Company',backref='platform')

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(48),primary_key=True)
    name = db.Column(db.String(48))
    annualizedReturn = db.Column(db.String(48)) #年化收益率
    cycle = db.Column(db.String(48)) #投资周期
    remainAmount = db.Column(db.String(48)) #剩余额度
    platform_id = db.Column(db.String(48),db.ForeignKey('platform.id'))

class Company(db.Model):
    """新增公司信息"""
    __tablename__ = 'company'

    id = db.Column(db.String(48),primary_key=True)
    platformName = db.Column(db.String(48)) #冗余字段
    companyName = db.Column(db.String(48))
    legalRepresentative = db.Column(db.String(48))
    QQ = db.Column(db.String(48))
    phoneCustomer = db.Column(db.String(48))
    address = db.Column(db.String(128))
    noteSpecial = db.Column(db.Text)
    platform_id = db.Column(db.String(48),db.ForeignKey('platform.id'))

class News(db.Model):
    """新闻资讯模型"""
    __tablename__ = 'newses'

    id = db.Column(db.String(128),primary_key=True)
    title = db.Column(db.String(128),index=True) # 标题
    content = db.Column(db.Text) # 内容
    date_publish = db.Column(db.String(32),index=True) # 发布日期
    date_crawl = db.Column(db.String(32),index=True) # 收录日期
    agency_source = db.Column(db.String(128),index=True) # 版权所有
    author_source = db.Column(db.String(64),index=True) # 作者
    url_source = db.Column(db.String(128)) # 网址
    url_crawl = db.Column(db.Text) # 收录网址
    status = db.Column(db.String(32),default=0) # 状态
    cases = db.relationship('Case',backref='news')

class Case(db.Model):
    """案例模型"""
    __tablename__ = 'cases'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),index=True) # 标题
    date_start = db.Column(db.String(32),index=True) # 起始日期
    date_end = db.Column(db.String(32),index=True) # 截止日期
    location = db.Column(db.String(128),index=True) # 涉案地点
    persons_involved = db.Column(db.String(128),index=True) # 涉案人员
    company_involved = db.Column(db.String(128),index=True) # 公司信息
    means_description = db.Column(db.Text) # 诈骗手法描述
    victims = db.Column(db.String(128)) # 被害人信息
    momeny_involved = db.Column(db.String(128),index=True) # 涉案金额及描述
    agency = db.Column(db.String(128),index=True) # 执法机关
    courts = db.Column(db.String(128),index=True) # 判决机构
    sentence = db.Column(db.Text) # 判决结果
    keyword = db.Column(db.Text) # 本案关键词
    news_id = db.Column(db.Integer,db.ForeignKey('newses.id'))
    notes = db.Column(db.Text) # 备注

class User(UserMixin,db.Model):
    """用户模型"""
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128),index=True,unique=True) # 用户名,唯一
    email = db.Column(db.String(128),index=True,unique=True) # 注册邮箱,唯一
    password_hash = db.Column(db.String(128),index=True) # 密码摘要
    status = db.Column(db.String(32),default=False) # 用户状态,默认未激活
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id')) # 外键,角色id

    @property # 方法转化为属性,可以用.访问
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self,password):
        """只写属性"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        """验证密码"""
        return check_password_hash(self.password_hash,password)


class Role(db.Model):
    """角色模型"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True,index=True) # 角色名称,唯一
    # 同一角色对应的用户对象列表,backref向User模型添加role属性
    # role属性可以替代外键role_id访问Role模型
    users = db.relationship('User',backref='role')

class Area(db.Model):
    """行政区划模型"""
    __tablename__ = 'areas'

    id = db.Column(db.Integer,primary_key=True) # 系统默认键
    code = db.Column(db.String(32),unique=True,index=True) # 行政区划代码
    area_name = db.Column(db.String(32),index=True) # 名称
    level = db.Column(db.Integer) # 行政区划层级
    code_highlevel = db.Column(db.Integer) # 上级行政代码

class Document(db.Model):
    """判决文书"""
    __tablename__="documents"

    id = db.Column(db.String(128),primary_key=True) # url签名
    url = db.Column(db.String(128),index=True) # 判决书网址
    title = db.Column(db.String(128),index=True) # 标题
    location = db.Column(db.String(128),index=True) # 区域
    types = db.Column(db.String(128),index=True) # 定罪类型
    court = db.Column(db.String(128),index=True) # 判决法院
    document_code = db.Column(db.String(128),index=True) # 文书字号
    document_type = db.Column(db.String(128),index=True) # 文书类型
    conclusion_date = db.Column(db.String(64),index=True) # 审结日期
    proceeding = db.Column(db.String(64),index=True) # 审理程序
    trial_person = db.Column(db.String(64),index=True) # 审理人员
    judgment = db.Column(db.Text,index=True) # 判决书正文
    crawl_time = db.Column(db.String(32),index=True) # 收录时间


    @staticmethod
    def from_json(json_post):
        pass
        id = json_post.get('id')
        url = json_post.get('url')
        title = json_post.get('title')
        location = json_post.get('location')
        types = json_post.get('types')
        court = json_post.get('court')
        document_code = json_post.get('document_code')
        document_type = json_post.get('document_type')
        conclusion_date = json_post.get('conclusion_date')
        proceeding = json_post.get('proceeding')
        trial_person = json_post.get('trial_person')
        judgment = json_post.get('judgment')
        # 此处添加数据检查代码
        return Document(id=id,
                        url=url,
                        title=title,
                        location=location,
                        types=types,
                        court=court,
                        document_code=document_code,
                        document_type=document_type,
                        conclusion_date=conclusion_date,
                        proceeding=proceeding,
                        trial_person=trial_person,
                        judgment=judgment,
                        )
    def to_json(self):
        json_document = {'url':url_for('main.document_detail',id=self.id),
                         'title':self.title,
                         'court':self.court}
        return json_document


if __name__ == '__main__':
    pass
    db.create_all()
