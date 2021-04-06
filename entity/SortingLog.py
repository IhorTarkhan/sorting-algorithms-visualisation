from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortAlgorithmEnum import SortAlgorithmEnum


class SortingLog:
    """
        The Entity that storage in database
    """

    def __init__(self,
                 log_id: int or None,
                 algorithm: SortAlgorithmEnum,
                 initial_array_order: ArrayOrderEnum,
                 array_size: int,
                 time_usage: float,
                 size_usage: float):
        self.log_id = log_id
        self.algorithm = algorithm
        self.initial_array_order = initial_array_order
        self.array_size = array_size
        self.time_usage = time_usage
        self.size_usage = size_usage
