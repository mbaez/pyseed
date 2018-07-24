#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define la capa de servicios de la aplicación

@autor Maximiliano Báez
@contact mxbg.py@gmail.com
"""

from module.ws import *

if __name__ =="__main__" :
    app.run(host=app.config.get("app.host"), port=app.config.get("app.port"), debug=True)
