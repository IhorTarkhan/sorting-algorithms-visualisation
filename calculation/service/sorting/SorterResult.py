class SorterResult:
    """
        Data transfer object (DTO) to present time and memory-size usage of sorting
    """

    def __init__(self, time_used: float, memory_used: float):
        self.time_used = time_used
        self.memory_used = memory_used
