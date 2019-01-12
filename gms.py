#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: gms.py
@time: 2019/1/11 23:42
"""
from apps import create_app

app = create_app()


if __name__ == "__main__":
    app.run()
