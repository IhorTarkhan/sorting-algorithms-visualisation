from sort_utils.algoritms.BrickSorter import BrickSorter
from sort_utils.algoritms.BubbleSorter import BubbleSorter
from sort_utils.algoritms.CocktailSorter import CocktailSorter
from sort_utils.algoritms.MargeSorter import MargeSorter
from sort_utils.algoritms.QuickSorter import QuickSorter
from sort_utils.algoritms.RadixSorter import RadixSorter

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

brick = BrickSorter().benchmark(array)
bubble = BubbleSorter().benchmark(array)
cocktail = CocktailSorter().benchmark(array)
marge = MargeSorter().benchmark(array)
quick = QuickSorter().benchmark(array)
radix = RadixSorter().benchmark(array)

print('brick', brick)
print('bubble', bubble)
print('cocktail', cocktail)
print('marge', marge)
print('quick', quick)
print('radix', radix)
