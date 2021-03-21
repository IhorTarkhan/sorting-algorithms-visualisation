from pyatspi import SortOrder

from sort_utils.SorterResult import SorterResult


class AbstractSorter:
    def sort(self, initial_array: [int], sort_order: SortOrder) -> SorterResult:
        raise NotImplementedError("Please Implement this method")
