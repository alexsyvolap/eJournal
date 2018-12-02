from __future__ import print_function


import sqlalchemy as sa
import helper as help
from sqlalchemy.orm import Query


class Users(help.BaseModel):
    __tablename__ = 'users'
    __repr_attrs__ = ['id', 'fname', 'lname', 'sname', 'password', 'status']
    id = sa.Column(sa.String(25), primary_key=True)
    fname = sa.Column(sa.String(25))
    lname = sa.Column(sa.String(25))
    sname = sa.Column(sa.String(25))
    password = sa.Column(sa.String(25))
    status = sa.Column(sa.SmallInteger)

    token = sa.orm.relationship('Tokens')
    group = sa.orm.relationship('Group_User')


class Tokens(help.BaseModel):
    __tablename__ = 'tokens'
    __repr_attrs__ = ['id', 'user_id', 'token', 'date_life']
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.String(25), sa.ForeignKey('users.id'))
    token = sa.Column(sa.String(50))
    date_life = sa.Column(sa.DateTime)

    user = sa.orm.relationship('Users')


class Groups(help.BaseModel):
    __tablename__ = 'groups'
    __repr_attrs__ = ['id', 'name']
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(25))

    group_user = sa.orm.relationship('Group_User')


class Subjects(help.BaseModel):
    __tablename__ = 'subjects'
    __repr_attrs__ = ['id', 'name']
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(25))

    subjects_group = sa.orm.relationship('Subjects_Group')


class Group_User(help.BaseModel):
    __tablename__ = 'user_group'
    __repr_attrs__ = ['user_id', 'group_id']
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.String(25), sa.ForeignKey('users.id'))
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'))

    user = sa.orm.relationship('Users')
    group = sa.orm.relationship('Groups')


class Subjects_Group(help.BaseModel):
    __tablename__ = 'subjects_group'
    __repr_attrs__ = ['group_id', 'subject_id']
    id = sa.Column(sa.Integer, primary_key=True)
    group_id = sa.Column(sa.Integer, sa.ForeignKey('groups.id'))
    subject_id = sa.Column(sa.String(25), sa.ForeignKey('subjects.id'))

    subject = sa.orm.relationship('Subjects')
    group = sa.orm.relationship('Groups')
