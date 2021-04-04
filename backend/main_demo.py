from backend.service.array_generate.ArrayFactory import generate_number_array
from backend.service.array_generate.ArrayOrderEnum import ArrayOrderEnum
from backend.service.sorting.algoritms.BrickSorter import BrickSorter
from backend.service.sorting.algoritms.BubbleSorter import BubbleSorter
from backend.service.sorting.algoritms.CocktailSorter import CocktailSorter
from backend.service.sorting.algoritms.MargeSorter import MargeSorter
from backend.service.sorting.algoritms.QuickSorter import QuickSorter
from backend.service.sorting.algoritms.RadixSorter import RadixSorter

if __import__('__main__'):
    array = generate_number_array(1, 1000, 100, ArrayOrderEnum.RANDOM)

    brick = BrickSorter().benchmark(array)
    print('brick\t', brick)

    bubble = BubbleSorter().benchmark(array)
    print('bubble\t', bubble)

    cocktail = CocktailSorter().benchmark(array)
    print('cocktail', cocktail)

    marge = MargeSorter().benchmark(array)
    print('marge\t', marge)

    quick = QuickSorter().benchmark(array)
    print('quick\t', quick)

    radix = RadixSorter().benchmark(array)
    print('radix\t', radix)
