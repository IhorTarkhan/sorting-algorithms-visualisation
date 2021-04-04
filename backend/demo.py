from backend.db.sorting_logs_connector import create_table_if_not_exist, get_all_sorting_logs, create_sorting_log
from backend.entity.ArrayOrderEnum import ArrayOrderEnum
from backend.entity.SortAlgorithmEnum import SortAlgorithmEnum
from backend.entity.SortingLog import SortingLog

if __import__('__main__'):
    create_table_if_not_exist()
    logs = get_all_sorting_logs()
    new_log = SortingLog(None, SortAlgorithmEnum.RADIX, ArrayOrderEnum.RANDOM, 2, 3, 4)
    create_sorting_log(new_log)
