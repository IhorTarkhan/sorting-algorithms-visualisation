from backend.controller.benchmark_run import run_benchmark
from backend.service.array_generate.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    run_benchmark(1, 1000, 100, ArrayOrderEnum.RANDOM)
