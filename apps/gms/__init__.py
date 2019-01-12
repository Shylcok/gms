#!/usr/bin/env python
# encoding: utf-8

"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: __init__.py.py
@time: 2019/1/11 22:41
"""
from flask import Blueprint

gms = Blueprint('main', __name__)
from . import views
