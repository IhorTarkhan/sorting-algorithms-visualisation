from sorting_techniques import pysort


class PySorter:
    __instance = pysort.Sorting()

    def __init__(self):
        raise PermissionError("Not permit to create object")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = pysort.Sorting()
        return cls.__instance
