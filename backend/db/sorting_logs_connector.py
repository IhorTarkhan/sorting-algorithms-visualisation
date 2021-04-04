from typing import List

from backend.db.Connector import Connector
from backend.service.sorting.SortAlgorithmEnum import SortAlgorithmEnum
from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortingLog import SortingLog


def create_table_if_not_exist():
    Connector.execute('CREATE TABLE IF NOT EXISTS sorting_logs (' +
                      'log_id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,' +
                      'algorithm           VARCHAR(30) NOT NULL,' +
                      'initial_array_order VARCHAR(30) NOT NULL,' +
                      'array_size          INT         NOT NULL,' +
                      'time_usage          FLOAT       NOT NULL,' +
                      'size_usage          FLOAT       NOT NULL);')


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
        'INSERT INTO sorting_logs (algorithm, initial_array_order, array_size, time_usage, size_usage) ' +
        'VALUE ' + save_brackets_generate(new_log) + ';'
    )


def create_sorting_logs(new_logs: List[SortingLog]):
    brackets = ''
    length = len(new_logs)
    for it in range(length):
        brackets += save_brackets_generate(new_logs[it])
        if it != length - 1:
            brackets += ', '

    Connector.execute(
        'INSERT INTO sorting_logs (algorithm, initial_array_order, array_size, time_usage, size_usage) ' +
        'VALUES ' + brackets + ';'
    )


def save_brackets_generate(log: SortingLog):
    return '(\'{}\', \'{}\', {}, {}, {})'.format(
        log.algorithm.value,
        log.initial_array_order.value,
        log.array_size,
        log.time_usage,
        log.size_usage)
