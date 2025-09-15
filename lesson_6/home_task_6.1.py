class ReverseFileIterator:
    """
    Iterator to read a file line by line in reverse order.

    Usage:
        for line in ReverseFileIterator("filename.txt"):
            print(line)

    This iterator reads all lines into memory, then iterates
    from the last line to the first line.
    """

    def __init__(self, filename):
        """
        Initialize the iterator with the filename.

        Args:
            filename (str): Path to the text file.
        """
        with open(filename, "r", encoding="utf-8") as f:
            self.lines = f.readlines()  # Read all lines into a list
        self.index = len(self.lines) - 1  # Start from the last line

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Return the next line in reverse order.

        Raises:
            StopIteration: When all lines have been returned.
        """
        if self.index < 0:
            raise StopIteration  # No more lines to return
        line = self.lines[self.index].rstrip("\n")  # Remove newline character
        self.index -= 1  # Move to the previous line
        return line


# Example usage
for line in ReverseFileIterator("test.txt"):
    print(line)
