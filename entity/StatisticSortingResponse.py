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
                 ascending_time: float or None,
                 random_time: float or None,
                 descending_time: float or None,
                 ascending_size: float or None,
                 random_size: float or None,
                 descending_size: float or None):
        self.algorithm = algorithm
        self.array_size = array_size
        self.ascending_time = ascending_time
        self.random_time = random_time
        self.descending_time = descending_time
        self.ascending_size = ascending_size
        self.random_size = random_size
        self.descending_size = descending_size
