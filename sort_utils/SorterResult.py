from float_utils.FloatUtil import get_pretty


class SorterResult:
    def __init__(self, time_used: float, memory_used: float):
        self.time_used = time_used
        self.memory_used = memory_used

    def __str__(self):
        return f'[{get_pretty(self.time_used * 1000)} ms, {get_pretty(self.memory_used)} cu]'
