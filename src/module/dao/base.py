#! /usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2

class QueryDao(object):

    def fetch(self):
        """
        Se encarga de obtener todos los recursos de la base de datos.

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        pass

    def get(self, id):
        """
        Se encarga de obtener los datos de un recurso por id

        @rtype  Dictionaries
        @return Un diccionario con el resultado de la consulta
        """
        pass


    def insert(self, args={}):
        """
        Se encarga de persitir un recurso

        @type args : Dictionaries
        @param args: Un diccionario con los datos del recurso.

        """
        pass

    def update(self, args={}):
        """
        Se encarga de actualizar los datos de un recurso

        @type args : Dictionaries
        @param args: Un diccionario con los datos del recurso.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        pass

    def delete(self, args={}):
        """
        Se encarga de borrar un recurso

        @type args : Dictionaries
        @param args: Un diccionario con los datos del recurso.

        @rtype  Cursor
        @return Un cursor con el estado de la operación
        """
        pass

class BaseDao (QueryDao):
    """
    DAO base, implementa la conexión a la base de datos y los metodos CRUD base
    para las entidades.

    @autor Maximiliano Báez
    @contact mxbg.py@gmail.com
    """
    @property
    def conn(self):
        """
        Referencia a la conexión a la base de datos
        """
        return self.__conn

    @conn.setter
    def conn(self, value):
        """
        Seter del conector de la base de datos
        """
        self.__conn = value


    def __init__(self, config):
        """
        Constructor del dao base.
        """
        self.__conn = psycopg2.connect(database=config.get("db.name"),\
                                       user=config.get("db.user"),\
                                       password=config.get("db.password"),\
                                       host=config.get("db.host"), \
                                       port=config.get("db.port"));

        self.conn.autocommit = True

    def query(self, query_string, args={}, is_many=False):
        """
        Este método se encarga de construir la consulta sql definida en
        `query_string`, establce la conexión en la base de datos y
        ejecuta la consulta.

            SELECT * FROM tabla WHERE id = :id

        @type query_string : String
        @param query_string: La referencia al cursor de la consulta.

        @type args : Dictionaries
        @param args: Un diccionario con los parametros del query.

        @type insert_many : Boolean
        @param insert_many: True para activar el executemany.

        @rtype  Cursor
        @return La referencia al cursor de la consulta.
        """

        cursor = self.conn.cursor()
        if not is_many:
            cursor.execute(query_string, args)
        else:
            cursor.executemany(query_string, args)
        return cursor

    def to_dict(self, dbcursor):
        """
        Se encarga de procesar el cusor y generar un diccionario con los
        datos obtenidos del cursor. Las columnas de los campos del cursor
        son utilizadas como claves de diccionario.

        @type dbcursor : Cursor
        @param dbcursor : La referencia al cursor de la consulta.

        @rtype  Dictionaries
        @return Un diccionario con los datos del cursor.
        """
        # se obtienen todos los datos
        results = dbcursor.fetchall()
        if len(results) < 1:
            return results

        # se genera el array de resultados a partir de cursor
        rownum = 0
        for row in results:
            dictrow = {}
            dictnum = 0
            for col in dbcursor.description:
                dictrow[col[0]] = row[dictnum]
                dictnum += 1
            results[rownum] = dictrow
            rownum += 1

        dbcursor.close()
        # se retorna la lista de resultados
        return results
