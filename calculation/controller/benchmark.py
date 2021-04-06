from typing import List
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/aaade/Desktop/programs/OOP/sorting-algorithms-visualisation')
from calculation.db.sorting_logs_connector import create_sorting_logs, get_average_logs
from calculation.service.array_generate.ArrayFactory import generate_number_array
from calculation.service.sorting.SortAlgorithmSingleton import SortAlgorithmSingleton
from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortAlgorithmEnum import SortAlgorithmEnum
from entity.SortingLog import SortingLog
from entity.StatisticSortingResponse import StatisticSortingResponse


def run_benchmark(min_val: int, max_val: int, size: int, order: ArrayOrderEnum) \
        -> List[SortingLog]:
    """
        Implementation Model–view–controller Design Pattern

        ...

        Trying to implement MVC pattern, separate program for 'Frontend' and 'Backend',
        this is controller part - the mediator between User interface and calculation interface

        ...

        This is endpoint for UI part. By this endpoint UI can interact with 'calculation' part.
        Function that run all available sorting algorithm, calculate time and memory-size-usage,
        save this data to database as logs
    """
    array = generate_number_array(min_val, max_val, size, order)

    def log_benchmark(algorithm: SortAlgorithmEnum) -> SortingLog:
        result = SortAlgorithmSingleton.get_sorter(algorithm).benchmark(array)
        return SortingLog(None, algorithm, order, size, result.time_used, result.memory_used)

    brick_log = log_benchmark(SortAlgorithmEnum.BRICK)
    bubble_log = log_benchmark(SortAlgorithmEnum.BUBBLE)
    cocktail_log = log_benchmark(SortAlgorithmEnum.COCKTAIL)
    marge_log = log_benchmark(SortAlgorithmEnum.MERGE)
    quick_log = log_benchmark(SortAlgorithmEnum.QUICK)
    radix_log = log_benchmark(SortAlgorithmEnum.RADIX)

    new_logs = [brick_log, bubble_log, cocktail_log, marge_log, quick_log, radix_log]
    create_sorting_logs(new_logs)
    return new_logs


def get_statistic() -> List[StatisticSortingResponse]:
    """
        Implementation Model–view–controller Design Pattern

        ...

        Trying to implement MVC pattern, separate program for 'Frontend' and 'Backend',
        this is controller part - the mediator between User interface and calculation interface

        ...

        This is endpoint for UI part. By this endpoint UI can interact with 'calculation' part.
        Function that return statistic of all ever running sorts with calculating average
        time and memory-size-usage
    """
    avg_logs = get_average_logs()
    response_list: List[StatisticSortingResponse] = []
    for log in avg_logs:
        match_one_list = list(
            filter(lambda it: it.array_size == log.size and it.algorithm == log.algorithm, response_list))
        if len(match_one_list) == 0:
            match_one = StatisticSortingResponse(log.algorithm, log.size, None, None, None, None, None, None)
            response_list.append(match_one)
        else:
            match_one = match_one_list[0]

        if log.order == ArrayOrderEnum.ASC:
            match_one.ascending_time = log.avg_time
            match_one.ascending_size = log.avg_size
        elif log.order == ArrayOrderEnum.RANDOM:
            match_one.random_time = log.avg_time
            match_one.random_size = log.avg_size
        elif log.order == ArrayOrderEnum.DESC:
            match_one.descending_time = log.avg_time
            match_one.descending_size = log.avg_size

    return response_list
