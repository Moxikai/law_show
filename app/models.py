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

if __name__ == '__main__':
    pass
    db.create_all()
