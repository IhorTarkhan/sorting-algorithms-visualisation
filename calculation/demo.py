from controller.benchmark import run_benchmark
from db.sorting_logs_connector import create_table_if_not_exist

from entity.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    """
        Function to demonstrate how to use controllers
    """
    create_table_if_not_exist()
    for i in range(10):
        print('{}%'.format(i * 10))
        for size in range(1, 101):
            run_benchmark(1, 100, size, ArrayOrderEnum.ASC)
            run_benchmark(1, 100, size, ArrayOrderEnum.RANDOM)
            run_benchmark(1, 100, size, ArrayOrderEnum.DESC)
    print('100%')
