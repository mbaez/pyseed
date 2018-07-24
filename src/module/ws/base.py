#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Define la capa de servicios de la aplicación

@autor Maximiliano Báez
@contact mxbg.py@gmail.com
"""
from bottle import Bottle, route, request, abort, response
import json
# se configura instancia la aplicación
app = Bottle()
# carga las configuracioones del archivo .ini
app.config.load_config("application.ini")

class WS (object):

    def __init__(self, ctrl):
        self.ctrl = ctrl;

    def crear(self):
        response.content_type="application/json"
        data = json.load(request.body)
        return self.ctrl.crear(data);

    def listar(self, args={}):
        response.content_type="application/json"
        lista = self.ctrl.listar(args)
        return json.dumps(lista);

    def get(self, id):
        response.content_type="application/json"
        data = self.ctrl.obtener(id);
        return json.dumps(data)

    def actualizar(self, id):
        response.content_type="application/json"
        data = json.load(request.body)
        udp = self.ctrl.actualizar(data);
        return json.dumps.data();


@app.route('/404')
def error():
    return abort(404)
