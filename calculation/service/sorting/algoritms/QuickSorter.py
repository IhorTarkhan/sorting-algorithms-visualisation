import sys

from calculation.service.sorting.algoritms.AbstractSorter import AbstractSorter
from calculation.util.PySorter import PySorter


class QuickSorter(AbstractSorter):
    """
        Implementation Mediator Pattern

        ...

        This class - is a wrapper over external library.
        Implementation hide implementation and adding benchmark functionality
    """

    @staticmethod
    def sort_func(array):
        sys.setrecursionlimit(len(array) + 100)
        PySorter.get_instance().quickSort(array, 0, len(array) - 1)

    def __init__(self):
        super().__init__(self.sort_func)
