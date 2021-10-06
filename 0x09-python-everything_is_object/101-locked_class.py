class LockedClass:
    """
    This class is a locked class
    """
    __slots__ = ['first_name']

c = LockedClass()
print(c.__dict__())