from sort_utils.SorterResult import SorterResult
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class BubbleSorter(AbstractSorter):
    def sort(self, initial_array: [int]) -> SorterResult:
        # Your logic
        # Please do not sort initial_array, left it unsorted
        return SorterResult(time=5, size=50)
