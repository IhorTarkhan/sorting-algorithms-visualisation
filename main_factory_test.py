from array_generate_utils.ArrayFactory import generate_number_array
from array_generate_utils.ArrayOrderEnum import ArrayOrderEnum
from sort_utils.algoritms.BrickSorter import BrickSorter
from sort_utils.algoritms.BubbleSorter import BubbleSorter
from sort_utils.algoritms.CocktailSorter import CocktailSorter
from sort_utils.algoritms.MargeSorter import MargeSorter
from sort_utils.algoritms.QuickSorter import QuickSorter
from sort_utils.algoritms.RadixSorter import RadixSorter

array = generate_number_array(1, 1000, 100, ArrayOrderEnum.RANDOM)

brick = BrickSorter().benchmark(array)
print('brick', brick)

bubble = BubbleSorter().benchmark(array)
print('bubble', bubble)

cocktail = CocktailSorter().benchmark(array)
print('cocktail', cocktail)

marge = MargeSorter().benchmark(array)
print('marge', marge)

quick = QuickSorter().benchmark(array)
print('quick', quick)

radix = RadixSorter().benchmark(array)
print('radix', radix)
