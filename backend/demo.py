from backend.controller.benchmark_run import run_benchmark
from backend.db.sorting_logs_connector import \
    create_table_if_not_exist
from entity.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    create_table_if_not_exist()
    for size in range(100):
        for iteration in range(100):
            print('size={};\t\titeration={}'.format(size, iteration))
            run_benchmark(1, 100, 100, ArrayOrderEnum.RANDOM)
