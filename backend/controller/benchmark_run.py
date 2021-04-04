from backend.service.array_generate.ArrayFactory import generate_number_array
from backend.service.array_generate.ArrayOrderEnum import ArrayOrderEnum
from backend.service.sorting.SortAlgorithmEnum import SortAlgorithmEnum
from backend.service.sorting.SortAlgorithmSingleton import SortAlgorithmSingleton


def run_benchmark(min_val: int, max_val: int, size: int, order: ArrayOrderEnum):
    array = generate_number_array(min_val, max_val, size, order)

    brick_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.BRICK).benchmark(array)
    print('brick\t', brick_result)

    bubble_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.BUBBLE).benchmark(array)
    print('bubble\t', bubble_result)

    cocktail_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.COCKTAIL).benchmark(array)
    print('cocktail', cocktail_result)

    marge_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.MARGE).benchmark(array)
    print('marge\t', marge_result)

    quick_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.QUICK).benchmark(array)
    print('quick\t', quick_result)

    radix_result = SortAlgorithmSingleton.get_sorter(SortAlgorithmEnum.RADIX).benchmark(array)
    print('radix\t', radix_result)
