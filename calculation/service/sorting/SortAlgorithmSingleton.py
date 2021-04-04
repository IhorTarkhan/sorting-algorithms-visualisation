from entity.SortAlgorithmEnum import SortAlgorithmEnum
from calculation.service.sorting.algoritms.AbstractSorter import AbstractSorter
from calculation.service.sorting.algoritms.BrickSorter import BrickSorter
from calculation.service.sorting.algoritms.BubbleSorter import BubbleSorter
from calculation.service.sorting.algoritms.CocktailSorter import CocktailSorter
from calculation.service.sorting.algoritms.MargeSorter import MargeSorter
from calculation.service.sorting.algoritms.QuickSorter import QuickSorter
from calculation.service.sorting.algoritms.RadixSorter import RadixSorter


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
