def my_len(obj):
    if hasattr(obj, "__len__"):
        return len(obj)
    else:
        count = 0
        for item in obj:
            count += 1
        return count


def my_sum(value):
    total = 0
    for item in value:
        total += item
    return total


def my_min(value):
    value = iter(value)
    try:
        minimum = next(value)
    except StopIteration:
        raise ValueError("my min() arg is an empty sequence")

    for item in value:
        if item < minimum:
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
