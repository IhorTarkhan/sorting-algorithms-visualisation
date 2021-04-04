from typing import List

from backend.db.Connector import Connector
from backend.entity.SortingLog import SortingLog


def create_table_if_not_exist():
    Connector.execute('CREATE TABLE IF NOT EXISTS sorting_logs (' +
                      'log_id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,' +
                      'algorithm           VARCHAR(30) NOT NULL,' +
                      'initial_array_order VARCHAR(30) NOT NULL,' +
                      'size                INT         NOT NULL,' +
                      'time_usage          INT         NOT NULL,' +
                      'size_usage          INT         NOT NULL);')


def get_all_sorting_logs() -> List[SortingLog]:
    response = []
    result_list = Connector.execute('SELECT * FROM sorting_logs;')
    for result in result_list:
        response.append(SortingLog(result[0], result[1], result[2], result[3], result[4], result[5]))
    return response
