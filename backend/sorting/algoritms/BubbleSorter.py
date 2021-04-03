from backend.sorting.SortingInstance import SortingInstance
from backend.sorting.algoritms.AbstractSorter import AbstractSorter


class BubbleSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: SortingInstance.get_instance().bubbleSort(array))
