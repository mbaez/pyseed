#! /usr/bin/env python
# -*- coding: utf-8 -*-
class BaseController (object):
    """
    Capa encargada de abstraer la lógica de negocios para la capa de servicios.

    @autor Maximiliano Báez
    @contact mxbg.py@gmail.com
    """
    @property
    def dao(self):
        """
        Referencia al DAO
        """
        return self.__dao

    def crear(self, args):
        """
        Encargada de crear un nuevo recurso, realizando un insert en la
        BD con los datos.
        """
        self.dao.insert(args);

    def listar(self, args={}):
        """
        Obtiene la lista de los recursos.
        """
        return self.dao.fetch();

    def get(self, id):
        """
        Obtiene un recurso por su id
        """
        return self.dao.get(id);

    def eliminar(self, id):
        """
        Se encarga de eliminar un recurso por su id
        """
        return self.dao.delete(id);

    def actualizar(self, args):
        """
        Actualiza los datos de un recurso
        """
        return self.dao.update(args);
