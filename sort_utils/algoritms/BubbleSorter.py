from pyatspi import SortOrder

from sort_utils.SorterResult import SorterResult
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class Bubble(AbstractSorter):
    def sort(self, initial_array: [int], sort_order: SortOrder) -> SorterResult:
        # Your logic
        # Please do not sort initial_array, left it unsorted
        return SorterResult(time=5, size=50)
