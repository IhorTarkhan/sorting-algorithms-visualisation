from numpy import random

from array_generate_utils.ArrayOrderEnum import ArrayOrderEnum


def generate_number_array(min_val: int, max_val: int, size: int, order: ArrayOrderEnum) -> list:
    if min_val > max_val:
        raise ValueError('"min" value is bigger them "max" value')
    if size < 0:
        raise ValueError('"size" value must be positive')
    generated_array = random.randint(max_val - min_val, size=size) + min_val
    if order is ArrayOrderEnum.ASC:
        return sorted(generated_array)
    if order is ArrayOrderEnum.DESC:
        return sorted(generated_array, reverse=True)
    if order is ArrayOrderEnum.RANDOM:
        return list(generated_array)
    raise ValueError('"order" value is not supported')


print(generate_number_array(1, 25, 9, ArrayOrderEnum.DESC))
print(generate_number_array(1, 25, 9, ArrayOrderEnum.ASC))
print(generate_number_array(1, 25, 9, ArrayOrderEnum.RANDOM))
