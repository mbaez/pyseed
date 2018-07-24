#! /usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import Bottle, route, request, abort, response
from module.controller import AuthorController
from module.ws.base import *

"""
Capa de servicios para las operaciones CRUD de los usuarios
"""
author_ctr =  AuthorController(app.config);
author_ws = WS(author_ctr);

@app.post('/author')
def crear_usuario():
    return author_ws.crear();

@app.get('/author')
def listar_usuarios():
    return author_ws.listar();

@app.get('/author/<id>')
def get_usuario(id):
    return author_ws.get(id);

@app.put('/author/<id>')
def actualizar_usuario(id):
    return author_ws.actualizar(id);
