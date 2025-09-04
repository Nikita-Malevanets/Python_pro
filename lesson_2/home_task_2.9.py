def memoize(function_to_cache):
    """
    A simple memoization decorator to cache function results.
    Stores results in a dictionary to avoid repeated calculations.
    """
    cache = {}  # dictionary to store cached results

    def wrapper(number: int) -> int:
        # Return cached result if it exists
        if number in cache:
            return cache[number]

        # Compute result, store it in cache, and return it
        result = function_to_cache(number)
        cache[number] = result
        return result

    return wrapper


def fibonacci(number: int) -> int:
    """
    Calculate the n-th Fibonacci number recursively.
    """
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
