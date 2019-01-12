#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: gendb.py
@time: 2019/1/11 22:48
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from apps import create_app, db