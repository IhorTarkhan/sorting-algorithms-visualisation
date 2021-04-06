import copy
import time

from memory_profiler import memory_usage

from calculation.service.sorting.SorterResult import SorterResult


def sorting_time(sort, initial_array):
    time_start = time.time()
    sort(copy.deepcopy(initial_array))
    time_stop = time.time()
    different = time_stop - time_start
    return different


def sorting_size(sort, initial_array):
    array_copy = copy.deepcopy(initial_array)
    return sum(memory_usage(lambda: sort(array_copy)))


class AbstractSorter:
    """
        Implementation Polymorphism (OOP)

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
