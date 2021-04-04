from backend.service.sorting.SortingInstance import SortingInstance
from backend.service.sorting.algoritms.AbstractSorter import AbstractSorter


class CocktailSorter(AbstractSorter):
    def __init__(self):
        super().__init__(lambda array: SortingInstance.get_instance().cocktailSort(array))
