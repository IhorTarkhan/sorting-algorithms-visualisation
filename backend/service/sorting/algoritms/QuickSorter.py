from backend.util.PySorter import PySorter
from backend.service.sorting.algoritms.AbstractSorter import AbstractSorter


class QuickSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: PySorter.get_instance().quickSort(array, 0, len(array) - 1))
