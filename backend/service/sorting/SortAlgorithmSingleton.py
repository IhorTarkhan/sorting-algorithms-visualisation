from backend.service.sorting.SortAlgorithmEnum import SortAlgorithmEnum
from backend.service.sorting.algoritms.AbstractSorter import AbstractSorter
from backend.service.sorting.algoritms.BrickSorter import BrickSorter
from backend.service.sorting.algoritms.BubbleSorter import BubbleSorter
from backend.service.sorting.algoritms.CocktailSorter import CocktailSorter
from backend.service.sorting.algoritms.MargeSorter import MargeSorter
from backend.service.sorting.algoritms.QuickSorter import QuickSorter
from backend.service.sorting.algoritms.RadixSorter import RadixSorter


class SortAlgorithmSingleton:
    __brickSorter = BrickSorter()
    __bubbleSorter = BubbleSorter()
    __cocktailSorter = CocktailSorter()
    __margeSorter = MargeSorter()
    __quickSorter = QuickSorter()
    __radixSorter = RadixSorter()

    @classmethod
    def get_sorter(cls, algorithm: SortAlgorithmEnum) -> AbstractSorter:
        if algorithm is SortAlgorithmEnum.BRICK:
            return cls.__brickSorter
        if algorithm is SortAlgorithmEnum.BUBBLE:
            return cls.__bubbleSorter
        if algorithm is SortAlgorithmEnum.COCKTAIL:
            return cls.__cocktailSorter
        if algorithm is SortAlgorithmEnum.MARGE:
            return cls.__margeSorter
        if algorithm is SortAlgorithmEnum.QUICK:
            return cls.__quickSorter
        if algorithm is SortAlgorithmEnum.RADIX:
            return cls.__radixSorter
        raise ValueError('"order" value is not supported')
