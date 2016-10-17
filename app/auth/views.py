#coding:utf-8
"""
auth蓝本视图
"""

from flask import render_template,redirect,request,url_for,flash
from flask_login import login_user,logout_user,login_required,current_user

from . import auth
from ..models import User
from .forms import LoginForm,RegisterForm
from .. import db
from ..email import send_email

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
        token = user.generate_confirmation_token()
        send_email(user.email,'激活账户',
                   'auth/email/confirm',user=user,token=token)
        flash('激活邮件已发送到您的邮箱！')
        return redirect(url_for('main.index'))
    return render_template('auth/register.html',form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    """邮箱验证"""
    if current_user.confirmed:
        pass
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('您已确认账户')
    else:
        flash('确认链接已失效或者过期！')
    return redirect(url_for('main.index'))



