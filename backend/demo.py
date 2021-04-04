from backend.controller.benchmark_run import run_benchmark
from entity.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    run_benchmark(1, 100, 1000, ArrayOrderEnum.RANDOM)
