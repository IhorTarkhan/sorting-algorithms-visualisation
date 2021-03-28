import copy
import time

from sort_utils.SorterResult import SorterResult
from sort_utils.SortingObject import SortingObject
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class BrickSorter(AbstractSorter):
    def sort(self, initial_array: [int]) -> SorterResult:
        time_start = time.time()
        SortingObject.get_instance().brickSort(copy.copy(initial_array))
        time_stop = time.time()
        return SorterResult(time=(time_stop - time_start))
