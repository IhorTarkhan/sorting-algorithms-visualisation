from entity.SortAlgorithmEnum import SortAlgorithmEnum


class StatisticSortingResponse:
    """
        Statistic data transfer object (DTO), contains
            - sorting type (Bubble, Merge, etc)
            - size of array that was sorted in this way
            - three times of this sort (in 'best', 'avg', 'worst' cases)
    """

    def __init__(self,
                 algorithm: SortAlgorithmEnum,
                 array_size: int,
                 best_time: float or None,
                 average_time: float or None,
                 worst_time: float or None,
                 best_size: float or None,
                 average_size: float or None,
                 worst_size: float or None):
        self.algorithm = algorithm
        self.array_size = array_size
        self.best_time = best_time
        self.average_time = average_time
        self.worst_time = worst_time
        self.best_size = best_size
        self.average_size = average_size
        self.worst_size = worst_size
