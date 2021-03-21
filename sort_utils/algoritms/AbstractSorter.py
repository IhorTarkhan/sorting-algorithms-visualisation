from sort_utils.SorterResult import SorterResult


class AbstractSorter:
    def sort(self, initial_array: [int]) -> SorterResult:
        raise NotImplementedError("Please Implement this method")
