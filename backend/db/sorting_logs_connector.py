from typing import List

from backend.db.Connector import Connector
from backend.entity.ArrayOrderEnum import ArrayOrderEnum
from backend.entity.SortAlgorithmEnum import SortAlgorithmEnum
from backend.entity.SortingLog import SortingLog


def create_table_if_not_exist():
    Connector.execute('CREATE TABLE IF NOT EXISTS sorting_logs (' +
                      'log_id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,' +
                      'algorithm           VARCHAR(30) NOT NULL,' +
                      'initial_array_order VARCHAR(30) NOT NULL,' +
                      'array_size          INT         NOT NULL,' +
                      'time_usage          INT         NOT NULL,' +
                      'size_usage          INT         NOT NULL);')


def get_all_sorting_logs() -> List[SortingLog]:
    response = []
    result_list = Connector.execute('SELECT * FROM sorting_logs;')
    for result in result_list:
        response.append(
            SortingLog(result[0],
                       SortAlgorithmEnum(result[1]),
                       ArrayOrderEnum(result[2]),
                       result[3],
                       result[4],
                       result[5]))
    return response


def create_sorting_log(new_log: SortingLog):
    Connector.execute(
        ('INSERT INTO sorting_logs (algorithm, initial_array_order, array_size, time_usage, size_usage) ' +
         'VALUE (\'{}\', \'{}\', {}, {}, {});').format(
            new_log.algorithm.value,
            new_log.initial_array_order.value,
            new_log.array_size,
            new_log.time_usage,
            new_log.size_usage))
