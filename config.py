#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: config.py
@time: 2019/1/11 22:48
"""
password = input('请输入数据库密码:\n')
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://JYFelt:%s@127.0.0.1:3306/management" % password
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = '1werw3@#$@#%$^%&^%&^*&(*(()3he6'
BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

UPLOAD_FOLDER = ':\\uploadFile'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
