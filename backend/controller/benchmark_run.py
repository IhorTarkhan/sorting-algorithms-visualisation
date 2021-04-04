from backend.db.sorting_logs_connector import create_sorting_logs
from backend.service.array_generate.ArrayFactory import generate_number_array
from backend.service.sorting.SortAlgorithmEnum import SortAlgorithmEnum
from backend.service.sorting.SortAlgorithmSingleton import SortAlgorithmSingleton
from entity.ArrayOrderEnum import ArrayOrderEnum
from entity.SortingLog import SortingLog


def run_benchmark(min_val: int, max_val: int, size: int, order: ArrayOrderEnum):
    array = generate_number_array(min_val, max_val, size, order)

    def log_benchmark(algorithm: SortAlgorithmEnum) -> SortingLog:
        result = SortAlgorithmSingleton.get_sorter(algorithm).benchmark(array)
        return SortingLog(None, algorithm, order, size, result.time_used, result.memory_used)

    brick_log = log_benchmark(SortAlgorithmEnum.BRICK)
    bubble_log = log_benchmark(SortAlgorithmEnum.BUBBLE)
    cocktail_log = log_benchmark(SortAlgorithmEnum.COCKTAIL)
    marge_log = log_benchmark(SortAlgorithmEnum.MARGE)
    quick_log = log_benchmark(SortAlgorithmEnum.QUICK)
    radix_log = log_benchmark(SortAlgorithmEnum.RADIX)

    new_logs = [brick_log, bubble_log, cocktail_log, marge_log, quick_log, radix_log]
    create_sorting_logs(new_logs)
