import configparser
import sys

import mysql.connector

config = configparser.ConfigParser()
config.read(sys.argv[1])
mysql_config = config['mysql']


def execute(sql: str):
    database = mysql.connector.connect(**mysql_config)
    cursor = database.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    database.close()
    return result
