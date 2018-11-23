#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from App import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="127.0.0.1", port=port, debug=True)
