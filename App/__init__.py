# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
from logging.handlers import RotatingFileHandler
import datetime
import logging
from settings import HOST

app = Flask('App')
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = HOST['secret']
app.debug = False

#################### setup LOG ######################


handler = RotatingFileHandler('/var/log/eJournal/log-{0}.log'.format(datetime.date.today()), maxBytes=10000, backupCount=1)
app.logger.addHandler(handler)
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('werkzeug').addHandler(handler)
app.logger.setLevel(logging.WARNING)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)


import App.Controllers.LoginController
