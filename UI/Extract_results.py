from calculation.controller.benchmark import run_benchmark, get_statistic
from entity.ArrayOrderEnum import ArrayOrderEnum


class Extract_Results:
    def get_results(self, inputs, active):
        self.min = int(inputs[0]) if len(inputs[0]) > 0 else 0
        self.max = int(inputs[1]) if len(inputs[1]) > 0 else 0
        self.quantity = int(inputs[2]) if len(inputs[2]) > 0 else 0
        if active[0]:
            self.order = ArrayOrderEnum.RANDOM
        elif active[1]:
            self.order = ArrayOrderEnum.DESC
        else:
            self.order = ArrayOrderEnum.ASC

    def one_sample_results(self):
        return run_benchmark(self.min, self.max, self.quantity, self.order)

    def all_database_results(self):
        return get_statistic()

# ANDRUHUS, PLEASE FORMAT CODE - ctrl + l
# Bitte schön
