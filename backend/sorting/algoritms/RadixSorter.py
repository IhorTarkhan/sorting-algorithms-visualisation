from backend.sorting.SortingInstance import SortingInstance
from backend.sorting.algoritms.AbstractSorter import AbstractSorter


class RadixSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: SortingInstance.get_instance().radixSort(array))
