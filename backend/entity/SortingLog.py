from backend.entity.ArrayOrderEnum import ArrayOrderEnum
from backend.entity.SortAlgorithmEnum import SortAlgorithmEnum


class SortingLog(object):
    def __init__(self,
                 log_id: int,
                 algorithm: SortAlgorithmEnum,
                 initial_array_order: ArrayOrderEnum,
                 size: int,
                 time_usage: int,
                 size_usage: int):
        self.log_id = log_id
        self.algorithm = algorithm
        self.initial_array_order = initial_array_order
        self.size = size
        self.time_usage = time_usage
        self.size_usage = size_usage
