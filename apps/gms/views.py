#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: views.py
@time: 2019/1/11 22:42
"""
from flask import url_for, redirect, request, flash, render_template
from . import gms
from .forms import LoginForm


@gms.route('/baseinfo', methods=['GET'])
def getbaseinfo():
    return '测试'
