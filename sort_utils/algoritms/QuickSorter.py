import copy
import time

from sort_utils.SorterResult import SorterResult
from sort_utils.SortingObject import SortingObject
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class QuickSorter(AbstractSorter):
    def sort(self, initial_array: [int]) -> SorterResult:
        time_start = time.time()
        SortingObject.get_instance().quickSort(copy.copy(initial_array), 0, len(initial_array) - 1)
        time_stop = time.time()
        return SorterResult(time=(time_stop - time_start))
