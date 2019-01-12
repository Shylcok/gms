#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: forms.py
@time: 2019/1/11 23:19
"""
from wtforms import fields, validators
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = fields.StringField(label=u'管理员账号', validators=[validators.required()])
    password = fields.PasswordField(label=u'密码', validators=[validators.required()])
    remeber_me = fields.BooleanField('记住我')
    submit = fields.SubmitField('登陆')
