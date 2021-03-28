def get_in_milliseconds(time: float, accuracy: int = 3):
    return ('%.' + str(accuracy) + 'f') % (time * 1000)


def get_in_microseconds(time: float, accuracy: int = 3):
    return ('%.' + str(accuracy) + 'f') % (time * 1000000)
