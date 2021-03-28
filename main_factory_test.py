from sort_utils.algoritms.BrickSorter import BrickSorter
from sort_utils.algoritms.BubbleSorter import BubbleSorter
from sort_utils.algoritms.CocktailSorter import CocktailSorter
from sort_utils.algoritms.MargeSorter import MargeSorter
from sort_utils.algoritms.QuickSorter import QuickSorter
from sort_utils.algoritms.RadixSorter import RadixSorter
from time_utils.TimeUtil import get_in_milliseconds

array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

brick_time = BrickSorter().sort(array).time
bubble_time = BubbleSorter().sort(array).time
cocktail_time = CocktailSorter().sort(array).time
marge_time = MargeSorter().sort(array).time
quick_time = QuickSorter().sort(array).time
radix_time = RadixSorter().sort(array).time

print('brick_time', get_in_milliseconds(brick_time))
print('bubble_time', get_in_milliseconds(bubble_time))
print('cocktail_time', get_in_milliseconds(cocktail_time))
print('marge_time', get_in_milliseconds(marge_time))
print('quick_time', get_in_milliseconds(quick_time))
print('radix_time', get_in_milliseconds(radix_time))
