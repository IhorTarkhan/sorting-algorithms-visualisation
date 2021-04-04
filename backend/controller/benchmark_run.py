from backend.service.array_generate.ArrayFactory import generate_number_array
from backend.service.array_generate.ArrayOrderEnum import ArrayOrderEnum
from backend.service.sorting.algoritms.BrickSorter import BrickSorter
from backend.service.sorting.algoritms.BubbleSorter import BubbleSorter
from backend.service.sorting.algoritms.CocktailSorter import CocktailSorter
from backend.service.sorting.algoritms.MargeSorter import MargeSorter
from backend.service.sorting.algoritms.QuickSorter import QuickSorter
from backend.service.sorting.algoritms.RadixSorter import RadixSorter


def run_benchmark(min_val: int, max_val: int, size: int, order: ArrayOrderEnum):
    array = generate_number_array(min_val, max_val, size, order)

    brick_result = BrickSorter().benchmark(array)
    print('brick\t', brick_result)

    bubble_result = BubbleSorter().benchmark(array)
    print('bubble\t', bubble_result)

    cocktail_result = CocktailSorter().benchmark(array)
    print('cocktail', cocktail_result)

    marge_result = MargeSorter().benchmark(array)
    print('marge\t', marge_result)

    quick_result = QuickSorter().benchmark(array)
    print('quick\t', quick_result)

    radix_result = RadixSorter().benchmark(array)
    print('radix\t', radix_result)
