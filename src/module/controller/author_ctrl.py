#! /usr/bin/env python
# -*- coding: utf-8 -*-

from module.controller import BaseController
from module.dao import AuthorDao

class AuthorController (BaseController):
    """
    Controller relacionado a las operaciones correspondientes a los
    autores. Implementa las operaciones CRUD sobre las tablas.

    @autor Maximiliano Báez
    @contact mxbg.py@gmail.com
    """
    @property
    def dao(self):
        """
        Referencia al DAO de repositorios
        """
        return self.__dao


    def __init__(self, config):
        """
        Constructor de la clase, se encarga de inicializar el controller
        """
        self.__dao = AuthorDao(config)

    def listar_repositorios(self, id):
        """
        Obtiene la lista de los recursos.
        """
        return self.dao.get_repositories(id);
