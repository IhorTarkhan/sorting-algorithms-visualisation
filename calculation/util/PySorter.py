from sorting_techniques import pysort


class PySorter:
    """
        Implementation of Singleton Pattern

        ...

        This is wrapped library class 'pysort' to avoid multiple re-creation of sorting instance
    """
    __instance = None

    def __init__(self):
        raise PermissionError("Not permit to create object")

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = pysort.Sorting()
        return cls.__instance
