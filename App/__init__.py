# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask

app = Flask('project')
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'random'
app.debug = True
