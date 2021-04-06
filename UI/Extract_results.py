from calculation.controller.benchmark import run_benchmark, get_statistic
from entity.ArrayOrderEnum import ArrayOrderEnum


class Extract_Results:
    def get_results(self, inputs, active):
        self.min = inputs[0]
        self.max = inputs[1]
        self.quantity = inputs[2]
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
