from backend.util.PySorter import PySorter
from backend.service.sorting.algoritms.AbstractSorter import AbstractSorter


class BrickSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: PySorter.get_instance().brickSort(array))
