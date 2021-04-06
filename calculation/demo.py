from controller.benchmark import run_benchmark, get_statistic
from db.sorting_logs_connector import create_table_if_not_exist
import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'C:/Users/aaade/Desktop/programs/OOP/sorting-algorithms-visualisation')
from entity.ArrayOrderEnum import ArrayOrderEnum

if __import__('__main__'):
    """
        Function to demonstrate how to use controllers
    """
    create_table_if_not_exist()

    run_benchmark(1, 100, 100, ArrayOrderEnum.RANDOM)

    statistic_list = get_statistic()
    print(len(statistic_list))
