from typing import List

from backend.db.Connector import Connector
from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortAlgorithmEnum import SortAlgorithmEnum
from entity.SortingLog import SortingLog
from entity.StatisticSortingResponse import StatisticSortingResponse


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


class AverageStatistic:
    def __init__(self, algorithm: SortAlgorithmEnum, order: ArrayOrderEnum, size: int, avg_time: float,
                 avg_size: float):
        self.algorithm = algorithm
        self.order = order
        self.size = size
        self.avg_time = avg_time
        self.avg_size = avg_size


def get_average_statistic():
    result_list = Connector.execute(
        'SELECT algorithm, initial_array_order, array_size, AVG(time_usage) as avg_time, AVG(size_usage) as avg_size ' +
        'FROM sorting_logs ' +
        'GROUP BY algorithm, initial_array_order, array_size;')

    temp_list: List[AverageStatistic] = []
    for result in result_list:
        temp_list.append(
            AverageStatistic(SortAlgorithmEnum(result[0]), ArrayOrderEnum(result[1]), result[2], result[3], result[4]))

    response_list: List[StatisticSortingResponse] = []
    for temp in temp_list:

        match_one_list = list(
            filter(lambda it: it.array_size == temp.size and it.algorithm == temp.algorithm, response_list))
        if len(match_one_list) == 0:
            match_one = StatisticSortingResponse(temp.algorithm, temp.size, None, None, None, None, None, None)
            response_list.append(match_one)
        else:
            match_one = match_one_list[0]

        if temp.order == ArrayOrderEnum.ASC:
            match_one.forward_time = temp.avg_time
            match_one.forward_size = temp.avg_size
        elif temp.order == ArrayOrderEnum.RANDOM:
            match_one.average_time = temp.avg_time
            match_one.average_size = temp.avg_size
        elif temp.order == ArrayOrderEnum.DESC:
            match_one.backward_time = temp.avg_time
            match_one.backward_size = temp.avg_size

    return response_list


statistic = get_average_statistic()
print(statistic)
