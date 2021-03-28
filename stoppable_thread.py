from memory_profiler import memory_usage

from array_generate_utils.ArrayFactory import generate_number_array
from array_generate_utils.ArrayOrderEnum import ArrayOrderEnum
from sort_utils.algoritms.CocktailSorter import CocktailSorter


def f(size):
    CocktailSorter().sort(generate_number_array(100_000_000_000, 1_000_000_000_000, size, ArrayOrderEnum.RANDOM))


print(sum(memory_usage(lambda: f(1))))
print(sum(memory_usage(lambda: f(10))))
print(sum(memory_usage(lambda: f(100))))
print(sum(memory_usage(lambda: f(1000))))
print(sum(memory_usage(lambda: f(10000))))
