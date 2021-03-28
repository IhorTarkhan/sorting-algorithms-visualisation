from sort_utils.algoritms.BubbleSorter import BubbleSorter
from time_utils.TimeUtil import get_in_milliseconds

array = [1, 2, 5, 4]
time = BubbleSorter().sort(array).time
print(get_in_milliseconds(time))
print(array)
