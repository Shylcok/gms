#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: modelview.py
@time: 2019/1/11 23:49
"""
from flask_admin.contrib.sqla import ModelView


# 部门模型视图
class DepartmentModelView(ModelView):
    column_labels = {
        'DeptNo': u'部门编号',
        'DeptName': u'名称', }


# 院系模型视图
class FacultyModelView(ModelView):
    column_labels = {
        'FacultyNo': u'院系编号',
        'FacultyName': u'名称',
        'DeptNo': u'所属部门编号',
    }


# 职位模型视图
class PositionModelView(ModelView):
    column_labels = {
        'TeacherNo': u'教师编号',
        'TeacherName': u'名称',
        'Post': u'职位',
    }


# 科研模型视图
class ProjectModelView(ModelView):
    column_labels = {
        'ProjectNo': u'科研项目编号',
        'DeptNo': u'科研项目所属部门',
        'TeacherNo': u'负责教师编号',
        'TeacherName': u'教师姓名',
        'Report': u'上传标记',
        'Approval': u'审批标记',
        'Acceptance': u'验收标记',
        'ProjectNumbers': u'数量',
    }


# 教师模型视图
class TeacherModelView(ModelView):
    column_labels = {
        'TeacherNo': u'教师编号',
        'TeacherName': u'教师姓名',
        'TitleName': u'名称',
        'Sex': u'性别',
        'Contact': u'联系方式',
        'InFacultyNo': u'所属学院编号',
    }


# 职称模型视图
class TitleModelView(ModelView):
    column_labels = {
        'TeacherNo': u'教师编号',
        'TeacherName': u'名称',
        'TitleName': u'职称',
    }
