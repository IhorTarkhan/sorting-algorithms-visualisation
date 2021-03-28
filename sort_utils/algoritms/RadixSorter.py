from sort_utils.SortingObject import SortingObject
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class RadixSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: SortingObject.get_instance().radixSort(array))
