import copy
import time

import psutil

from calculation.service.sorting.SorterResult import SorterResult


def sorting_time(sort, initial_array):
    array_copy = copy.deepcopy(initial_array)
    time_start = time.time()
    sort(array_copy)
    time_stop = time.time()
    different = time_stop - time_start
    return different


def sorting_size(sort, initial_array):
    array_copy = copy.deepcopy(initial_array)
    before_use = psutil.virtual_memory().used
    sort(array_copy)
    after_use = psutil.virtual_memory().used
    different = after_use - before_use
    return abs(different)


class AbstractSorter:
    """
        Implementation Polymorphism (OOP)
        Implementation Template functional pattern

        ...

        This class - is a wrapper over sorting method.
        This class calculate time and memory-size usage of sorting algorithm
    """

    def __init__(self, sort):
        self.sort = sort

    def benchmark(self, initial_array: list) -> SorterResult:
        time_used = sorting_time(self.sort, initial_array)
        memory_used = sorting_size(self.sort, initial_array)
        return SorterResult(time_used, memory_used)
