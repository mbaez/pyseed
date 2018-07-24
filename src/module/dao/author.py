#! /usr/bin/env python
# -*- coding: utf-8 -*-
from module.dao.base import *

class AuthorDao(BaseDao):
    """
    DAO Author, implementa las operaciones CRUD sobre la tabla de authors.

    @autor Maximiliano Báez
    @contact mxbg.py@gmail.com
    """
    def fetch(self):
        """
        Se encarga de obtener todos los authores de la base de datos.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""SELECT * FROM author order by name"""
        cursor = self.query(sql_string)
        return self.to_dict(cursor)

    def get(self, id):
        """
        Se encarga de obtener los datos de un author especifico.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""
        SELECT * FROM author WHERE id= %(id)s
        """
        args = {"id" : id}
        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def get_repositories(self, id):
        """
        Se encarga de obtener la lista de repositorios asociados al author

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""

        SELECT DISTINCT r.* FROM author_repository ar
        JOIN repository r
        ON ar.id_repository = r.id
        WHERE ar.id_author = %(id)s
        """
        args = {"id" : id}
        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def get_by(self, email):
        """
        Se encarga de obtener los datos de un author especifico.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        sql_string="""
        SELECT * FROM author
        WHERE lower(email) = lower(%(email)s)
        OR lower(email) IN (
            SELECT lower(email) FROM author_alias
            WHERE alias = %(email)s
        )
        """
        args = {"email" : email}
        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def insert(self, args={}):
        """
        Se encarga de persitir el author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        """
        # se definie el query de la consulta.
        sql_string = """
        INSERT INTO author(name, email)
            VALUES (%(name)s,%(email)s)
        RETURNING id
        """

        cursor = self.query(sql_string, args)
        return self.to_dict(cursor)

    def update(self, args={}):
        """
        Se encarga de actualizar los datos de un author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        # se definie el query de la consulta.
        sql_string = """
        UPDATE author SET
            name=%(name)s,
            email=%(email)s,
        WHERE id= %(id)s
        """
        cursor = self.query(sql_string, args)
        return cursor

    def delete(self, args={}):
        """
        Se encarga de borrar un author

        @type args : Dictionaries
        @param args: Un diccionario con los datos del author.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        # se definie el query de la consulta.
        sql_string = """
        DELETE FROM author WHERE id= %(id)s
        """
        cursor = self.query(sql_string, args)
        return cursor
