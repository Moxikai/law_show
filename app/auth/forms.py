#coding:utf-8

"""
登录表单
"""
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo
from wtforms import ValidationError

from app.models import User
class LoginForm(Form):
    """登录表单"""
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log In')


class RegisterForm(Form):
    """注册表单"""
    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                                                                     '用户名只能使用字母、数字、_、.')])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password2',message='两次输入不匹配')])
    password2 = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        """自定义email验证函数"""
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册!')

    def validate_username(self,field):
        """自定义username验证函数"""
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册')