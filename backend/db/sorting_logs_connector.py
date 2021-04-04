from backend.db.Connector import Connector


def create_table_if_not_exist():
    Connector.execute('CREATE TABLE IF NOT EXISTS sorting_logs (' +
                      'id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,' +
                      'algorithm           VARCHAR(30) NOT NULL,' +
                      'initial_array_order VARCHAR(30) NOT NULL,' +
                      'size                INT         NOT NULL,' +
                      'time_usage          INT         NOT NULL,' +
                      'size_usage          INT         NOT NULL);')
