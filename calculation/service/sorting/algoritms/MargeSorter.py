from calculation.util.PySorter import PySorter
from calculation.service.sorting.algoritms.AbstractSorter import AbstractSorter


class MargeSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: PySorter.get_instance().mergeSort(array))
