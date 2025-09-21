def my_len(obj):
    """
    Return the number of elements in an object.

    If the object has __len__, use it.
    Otherwise, count elements manually using iteration.
    """
    if hasattr(obj, "__len__"):  # check if object has __len__ method
        return obj.__len__()

    count = 0
    for _ in obj:  # iterate over the object
        count += 1
    return count


def my_sum(iterable, start=0):
    """
    Return the sum of all elements in an iterable.

    Parameters:
    iterable -- any iterable object
    start -- initial value (default 0)
    """
    total = start
    for item in iterable:  # iterate and accumulate sum
        total += item
    return total


def my_min(iterable):
    """
    Return the minimum element from an iterable.

    Raises ValueError if the iterable is empty.
    """
    iterator = iter(iterable)
    try:
        minimum = next(iterator)  # take first element as initial minimum
    except StopIteration:
        raise ValueError("my_min() arg is an empty sequence")

    for item in iterator:  # iterate over remaining elements
        if item < minimum:  # update minimum if a smaller element is found
            minimum = item
    return minimum


def test_my_len():
    assert my_len([1, 2, 3]) == 3
    assert my_len([]) == 0
    assert my_len("hello") == 5


def test_my_sum():
    assert my_sum([1, 2, 3]) == 6
    assert my_sum([]) == 0
    assert my_sum([-1, 1, 10]) == 10


def test_my_min():
    assert my_min([5, 2, 9, 1]) == 1
    assert my_min("banana") == "a"
    assert my_min([42]) == 42
