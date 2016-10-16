#coding:utf-8
"""
测试api接口,新增document接口
"""
from flask import request,jsonify,url_for
from . import api
from ..models import Document
from .. import db


@api.route('/documents',methods=['POST'])
def new_document():
    pass
    document = Document.from_json(request.json)
    db.session.add(document)
    db.session.commit()
    return jsonify(document.to_json()),201
