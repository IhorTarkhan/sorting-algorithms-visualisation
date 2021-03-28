def get_in_milliseconds(time: float, accuracy: int = 3):
    return ('%.' + str(accuracy) + 'f') % (time * 1000)
