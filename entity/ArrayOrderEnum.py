from enum import Enum


class ArrayOrderEnum(Enum):
    """
        Most sorting algorithms have different sorting speeds for arrays of
        the same size and composition, but a different sequence.
        This Enum indicates the order of the elements when creating an array.
    """
    ASC = 'ASC'
    DESC = 'DESC'
    RANDOM = 'RANDOM'
