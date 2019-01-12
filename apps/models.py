#!/usr/bin/env python
# encoding: utf-8
"""
@version: python3.7
@author: JYFelt
@license: Apache Licence 
@contact: JYFelt@163.com
@site: https://blog.csdn.net/weixin_38034182
@software: PyCharm
@file: models.py
@time: 2019/1/11 23:35
"""
from . import db


# 部门表
class Department(db.Model):
    __tablename__ = 'Department'
    DeptNo = db.Column(db.Integer, primary_key=True)
    DeptName = db.Column(db.String(20), nullable=False)
    faculties = db.relationship("Faculty", backref="InDept", uselist=False)

    def __repr__(self):
        return '<Department %r>' % self.DeptName


# 院系表
class Faculty(db.Model):
    __tablename__ = 'Faculty'
    FacultyNo = db.Column(db.Integer, primary_key=True)
    FacultyName = db.Column(db.String(20), nullable=False)
    DeptNo = db.Column(db.Integer, db.ForeignKey("Department.DeptNo"), nullable=False)

    teachers = db.relationship("Teacher", backref="teacher")

    def __repr__(self):
        return '<Faculty %r>' % self.FacultyName


# 职位表（干啥的）
class Position(db.Model):
    __tablename__ = 'Position'

    TeacherNo = db.Column(db.Integer, db.ForeignKey("Teacher.TeacherNo"), primary_key=True)
    TeacherName = db.Column(db.String(20), nullable=False)
    Post = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Position %r>' % self.TeacherName


# 项目表
class Project(db.Model):
    __tablename__ = 'Project'
    ProjectNo = db.Column(db.Integer, primary_key=True)
    DeptNo = db.Column(db.Integer, nullable=False)
    TeacherNo = db.Column(db.Integer, db.ForeignKey("Teacher.TeacherNo"), nullable=False)
    TeacherName = db.Column(db.String(20), nullable=False)
    # 上传
    Report = db.Column(db.String(2), nullable=False)
    # 审批标记
    Approval = db.Column(db.String(2), nullable=False)
    # 验收标记
    Acceptance = db.Column(db.String(4), nullable=False)
    # 数量
    ProjectNumbers = db.Column(db.Integer, nullable=False)
    project_teacher_name = db.relationship("Teacher", backref='project_name')

    def __repr__(self):
        return '<Project %r>' % self.TeacherName


# 教师信息表
class Teacher(db.Model):
    __tablename__ = 'Teacher'
    TeacherNo = db.Column(db.Integer, primary_key=True, nullable=False)
    TeacherName = db.Column(db.String(20), nullable=False)
    # 职称
    TitleName = db.Column(db.String(20), nullable=False)
    Sex = db.Column(db.String(20), nullable=False)
    Contact = db.Column(db.String(14), nullable=False)
    InFacultyNo = db.Column(db.Integer, db.ForeignKey('Faculty.FacultyNo'), nullable=False)

    position = db.relationship("Position", backref="position")
    project = db.relationship("Project", backref="project")
    title = db.relationship("Title", backref="title")

    def __repr__(self):
        return '<Teacher %r>' % self.TeacherName


# 职称表（教授Or etc ）
class Title(db.Model):
    __tablename__ = 'Title'
    TeacherNo = db.Column(db.Integer, db.ForeignKey('Teacher.TeacherNo'), primary_key=True, nullable=False)
    TeacherName = db.Column(db.String(20), nullable=False)
    # 职称
    TitleName = db.Column(db.String(20), nullable=False)
    Title_teacher_name = db.relationship("Teacher", backref='title_teacher_name')

    def __repr__(self):
        return '<Title %r>' % self.TeacherName
