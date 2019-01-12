#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: __init__.py
@time: 2019/1/11 22:44
"""
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # 注册蓝图
    from apps.gms import gms
    app.register_blueprint(gms)

    # 注册db
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://JYFelt:wjy107723403...@127.0.0.1:3306/management"
    db.init_app(app)

    # 国际化
    from flask_babel import Babel
    babel = Babel(app)

    # 注册flask-admin
    from apps.models import Department, Faculty, Position, Project, Teacher, Title
    from apps.modelview import DepartmentModelView, FacultyModelView, PositionModelView, ProjectModelView, \
        TeacherModelView, TitleModelView
    admin = Admin(app, name="gms", template_mode='bootstrap3')
    admin.add_view(DepartmentModelView(Department, db.session, name="部门管理"))
    admin.add_view(FacultyModelView(Faculty, db.session, name="院系管理"))
    admin.add_view(PositionModelView(Position, db.session, name="职位管理"))
    admin.add_view(ProjectModelView(Project, db.session, name="项目管理"))
    admin.add_view(TeacherModelView(Teacher, db.session, name="教师信息管理"))
    admin.add_view(TitleModelView(Title, db.session, name="职称信息管理"))

    # 整合flask-login
    login_manager.init_app(app)

    return app
