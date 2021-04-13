from controller.benchmark import run_benchmark
from db.sorting_logs_connector import create_table_if_not_exist

from entity.ArrayOrderEnum import ArrayOrderEnum

if __name__ == "__main__":
    """
        Function to demonstrate how to use controllers
    """
    create_table_if_not_exist()
    for i in range(1000):
        print('{}%'.format(i / 10.0))
        for size in range(1, 101):
            run_benchmark(1, 100, size, ArrayOrderEnum.ASC)
            run_benchmark(1, 100, size, ArrayOrderEnum.RANDOM)
            run_benchmark(1, 100, size, ArrayOrderEnum.DESC)

        run_benchmark(1, 100, 333, ArrayOrderEnum.ASC)
        run_benchmark(1, 100, 333, ArrayOrderEnum.RANDOM)
        run_benchmark(1, 100, 333, ArrayOrderEnum.DESC)
        run_benchmark(1, 100, 667, ArrayOrderEnum.ASC)
        run_benchmark(1, 100, 667, ArrayOrderEnum.RANDOM)
        run_benchmark(1, 100, 667, ArrayOrderEnum.DESC)
        run_benchmark(1, 100, 1000, ArrayOrderEnum.ASC)
        run_benchmark(1, 100, 1000, ArrayOrderEnum.RANDOM)
        run_benchmark(1, 100, 1000, ArrayOrderEnum.DESC)
    print('100%')
