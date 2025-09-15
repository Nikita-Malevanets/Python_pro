import uuid


class UniqueIDIterator:
    """
    Iterator that generates unique identifiers (UUID4) one by one.

    Usage:
        uid_iter = UniqueIDIterator()
        for _ in range(5):
            print(next(uid_iter))

    Each call to `next()` returns a new unique ID.
    """

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Generate the next unique identifier.

        Returns:
            str: A new unique UUID4 string.
        """
        # Generate a random UUID (version 4)
        unique_id = uuid.uuid4()
        return str(unique_id)


# Example usage
uid_iter = UniqueIDIterator()
for _ in range(5):
    print(next(uid_iter))

