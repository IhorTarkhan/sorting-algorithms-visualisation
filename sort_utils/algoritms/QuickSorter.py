from sort_utils.SortingObject import SortingObject
from sort_utils.algoritms.AbstractSorter import AbstractSorter


class QuickSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: SortingObject.get_instance().quickSort(array, 0, len(array) - 1))
