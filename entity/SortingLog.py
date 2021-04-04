from entity.ArrayOrderEnum import ArrayOrderEnum
from backend.service.sorting.SortAlgorithmEnum import SortAlgorithmEnum


class SortingLog(object):
    def __init__(self,
                 log_id,
                 algorithm: SortAlgorithmEnum,
                 initial_array_order: ArrayOrderEnum,
                 array_size: int,
                 time_usage: int,
                 size_usage: int):
        self.log_id = log_id
        self.algorithm = algorithm
        self.initial_array_order = initial_array_order
        self.array_size = array_size
        self.time_usage = time_usage
        self.size_usage = size_usage
