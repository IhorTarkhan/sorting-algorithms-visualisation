from calculation.service.sorting.algoritms.AbstractSorter import AbstractSorter
from calculation.util.PySorter import PySorter


class QuickSorter(AbstractSorter):
    """
        Implementation Mediator Pattern

        ...

        This class - is a wrapper over external library.
        Implementation hide implementation and adding benchmark functionality
    """

    def __init__(self):
        super().__init__(lambda array: PySorter.get_instance().quickSort(array, 0, len(array) - 1))
