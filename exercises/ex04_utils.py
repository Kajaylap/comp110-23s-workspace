"""EX04 - list Utility Functions."""

__author__ = "730418782"


def all(list_int: list[int], number: int) -> bool:
    """Return bool to indicate if ints in the list are the same as given number."""
    index = 0
    while index < len(list_int):
        if list_int[index] != number:
            return False
        index = index + 1
    else:
        return True


def max(list_int: list[int]) -> int:
    """Max should return the largest in the List."""
    return max(list_int)


def is_equal(list_int: list[int], list_int2: list[int]) -> bool:
    """Return True if every element at every index is equal in both lists."""
    if list_int == list_int2:
        return True
    else:
        return False
