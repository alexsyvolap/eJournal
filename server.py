# -*- coding: utf-8 -*-
from settings import HOST
from App import app

if __name__ == '__main__':
    app.run(host=HOST['host'], port=HOST['port'], threaded=True)
