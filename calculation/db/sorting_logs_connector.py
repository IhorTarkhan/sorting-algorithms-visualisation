from typing import List

from calculation.db.AverageSortingLog import AverageSortingLog
from calculation.db.Connector import Connector
from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortAlgorithmEnum import SortAlgorithmEnum
from entity.SortingLog import SortingLog

table = 'sorting_logs'
# table = 'sorting_logs_populated'


def create_table_if_not_exist():
    """
        Guarantee existing of table 'sorting_logs'
        Recommend to add before your start your app
    """
    Connector.execute('CREATE TABLE IF NOT EXISTS ' + table + ' (' +
                      'log_id                  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,' +
                      'algorithm           VARCHAR(30) NOT NULL,' +
                      'initial_array_order VARCHAR(30) NOT NULL,' +
                      'array_size          INT         NOT NULL,' +
                      'time_usage          FLOAT       NOT NULL,' +
                      'size_usage          FLOAT       NOT NULL);')


def get_all_sorting_logs() -> List[SortingLog]:
    """
        Fetch all rows from database and present if in class format
    """
    response = []
    result_list = Connector.execute('SELECT * FROM ' + table + ';')
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
        'INSERT INTO ' + table + ' (algorithm, initial_array_order, array_size, time_usage, size_usage) ' +
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
        'INSERT INTO ' + table + ' (algorithm, initial_array_order, array_size, time_usage, size_usage) ' +
        'VALUES ' + brackets + ';'
    )


def save_brackets_generate(log: SortingLog):
    """
        Utility function, map class-entity to brackets-look to for insert operation sql
        Not run query in database
    """
    return '(\'{}\', \'{}\', {}, {}, {})'.format(
        log.algorithm.value,
        log.initial_array_order.value,
        log.array_size,
        log.time_usage,
        log.size_usage)


def get_average_logs() -> List[AverageSortingLog]:
    """
        Get all rows from database and calculate average time and memory-size for coinciding types of sorting
    """
    result_list = Connector.execute(
        'SELECT algorithm, initial_array_order, array_size, AVG(time_usage) as avg_time, AVG(size_usage) as avg_size ' +
        'FROM ' + table + ' ' +
        'GROUP BY algorithm, initial_array_order, array_size;')

    response_list: List[AverageSortingLog] = []
    for result in result_list:
        response_list.append(
            AverageSortingLog(SortAlgorithmEnum(result[0]), ArrayOrderEnum(result[1]), result[2], result[3], result[4]))
    return response_list
