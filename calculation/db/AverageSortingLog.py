from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortAlgorithmEnum import SortAlgorithmEnum


class AverageSortingLog:
    """
        Entity to present average time and memory-size types of sorting
    """

    def __init__(self,
                 algorithm: SortAlgorithmEnum,
                 order: ArrayOrderEnum,
                 size: int,
                 avg_time: float,
                 avg_size: float):
        self.algorithm = algorithm
        self.order = order
        self.size = size
        self.avg_time = avg_time
        self.avg_size = avg_size
