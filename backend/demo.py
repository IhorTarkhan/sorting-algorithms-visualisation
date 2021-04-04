from backend.controller.benchmark import run_benchmark, get_statistic
from backend.db.sorting_logs_connector import create_table_if_not_exist
from entity.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    create_table_if_not_exist()

    run_benchmark(1, 100, 100, ArrayOrderEnum.RANDOM)

    statistic_list = get_statistic()
    print(len(statistic_list))
