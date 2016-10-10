#!/usr/bin/env python
#coding:utf-8

"""
模型
"""

from . import db

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

class Case(db.Model):
    """案例模型"""
    __tablename__ = 'cases'

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),index=True) # 标题
    date = db.Column(db.String(128),index=True) # 时间
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
    notes = db.Column(db.Text) # 备注





if __name__ == '__main__':
    pass
    db.create_all()
