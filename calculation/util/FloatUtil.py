def get_pretty(value: float, accuracy: int = 3):
    """
        Small utility function to make float mor pretty
    """
    return ('%.' + str(accuracy) + 'f') % value
