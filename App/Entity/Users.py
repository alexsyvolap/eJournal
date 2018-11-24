from __future__ import print_function


import sqlalchemy as sa
import helper as help
from sqlalchemy.orm import Query


class Users(help.BaseModel):
    __tablename__ = 'users'
    __repr_attrs__ = ['id', 'fname', 'lname', 'sname', 'password', 'is_teacher']
    id = sa.Column(sa.String(25), primary_key=True)
    fname = sa.Column(sa.String(25))
    lname = sa.Column(sa.String(25))
    sname = sa.Column(sa.String(25))
    password = sa.Column(sa.String(25))
    is_teacher = sa.Column(sa.SmallInteger)

    token = sa.orm.relationship('Tokens')


class Tokens(help.BaseModel):
    __tablename__ = 'tokens'
    __repr_attrs__ = ['id', 'user_id', 'token', 'date_life']
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.String(25), sa.ForeignKey('users.id'))
    token = sa.Column(sa.String(50))
    date_life = sa.Column(sa.DateTime)

    user = sa.orm.relationship('Users')
