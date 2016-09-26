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

class Person(db.Model):
    __tablename__='person'

    id = db.Column(db.String(48),primary_key=True)
    abstracts = db.Column(db.Text)
    platform_id = db.Column(db.String(48),db.ForeignKey('platform.id'))



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
    persons = db.relationship('Person',backref='platform')

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.String(48),primary_key=True)
    name = db.Column(db.String(48))
    annualizedReturn = db.Column(db.String(48)) #年化收益率
    cycle = db.Column(db.String(48)) #投资周期
    remainAmount = db.Column(db.String(48)) #剩余额度
    platform_id = db.Column(db.String(48),db.ForeignKey('platform.id'))


if __name__ == '__main__':
    pass
    db.create_all()
