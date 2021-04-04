from entity.SortAlgorithmEnum import SortAlgorithmEnum


class StatisticSortingResponse:
    def __init__(self,
                 algorithm: SortAlgorithmEnum,
                 array_size: int,
                 forward_time: float or None,
                 average_time: float or None,
                 backward_time: float or None,
                 forward_size: float or None,
                 average_size: float or None,
                 backward_size: float or None):
        self.algorithm = algorithm
        self.array_size = array_size
        self.forward_time = forward_time
        self.average_time = average_time
        self.backward_time = backward_time
        self.forward_size = forward_size
        self.average_size = average_size
        self.backward_size = backward_size
