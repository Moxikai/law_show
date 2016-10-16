#coding:utf-8
"""
auth蓝本视图
"""

from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required

from . import auth
from ..models import User
from .forms import LoginForm,RegisterForm
from .. import db

@auth.route('/login',methods=["GET","POST"])
def login():
    """登录视图"""
    form = LoginForm()
    if form.validate_on_submit():
        """处理post数据"""
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            """不为空且密码通过验证"""
            login_user(user,form.remember_me.data) # 登入用户
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
    """退出"""
    logout_user()
    flash('你已经退出登录')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    """注册视图"""
    form = RegisterForm()
    if form.validate_on_submit():
        pass
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data,
                    )
        db.session.add(user)
        db.session.commit()
        flash('请稍后登陆！')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)




