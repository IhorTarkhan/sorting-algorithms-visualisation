from typing import List

from numpy import random

from entity.ArrayOrderEnum import ArrayOrderEnum


def generate_number_array(min_val: int, max_val: int, size: int, order: ArrayOrderEnum) -> List[int]:
    """
        Implementation of Factory Pattern

        ...

        This is function that receive parameters of array and generate respectively array
    """
    if min_val > max_val:
        raise ValueError('"min" value is bigger them "max" value')
    if size <= 0:
        raise ValueError('"size" value must be positive')

    generated_array = random.randint(max_val - min_val, size=size) + min_val
    if order is ArrayOrderEnum.ASC:
        return sorted(generated_array)
    if order is ArrayOrderEnum.DESC:
        return sorted(generated_array, reverse=True)
    if order is ArrayOrderEnum.RANDOM:
        return list(generated_array)
    raise ValueError('"order" value is not supported')
