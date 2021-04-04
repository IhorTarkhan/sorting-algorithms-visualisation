import configparser
import sys

import mysql.connector


class Connector:
    config = configparser.ConfigParser()
    config.read(sys.argv[1])
    mysql_config = config['mysql']

    @classmethod
    def execute(cls, sql: str):
        database = mysql.connector.connect(**cls.mysql_config)
        cursor = database.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        database.commit()
        cursor.close()
        database.close()
        return result
