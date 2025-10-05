import os


class BackupFile:
    """
    A context manager for automatic file backup.

    When entering the 'with' block:
        - creates a backup of the file (filename.bak) if it exists.

    When exiting the block:
        - if no errors occurred, the backup is deleted;
        - if an error occurred, the original file is restored from the backup.
    """

    def __init__(self, filename):
        """
        Constructor of the class.
        :param filename: the original file name
        """
        self.filename = filename
        self.backup_filename = filename + ".bak"  # name of the backup file

    def __enter__(self):
        """
        Entering the 'with' block. Creates a backup copy of the file.
        :return: the file name to use inside the block
        """
        if os.path.exists(self.filename):
            # Read the content of the original file
            with open(self.filename, "r", encoding="utf-8") as f:
                data = f.read()
            # Write the content to the backup file
            with open(self.backup_filename, "w", encoding="utf-8") as f:
                f.write(data)
        return self.filename

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exiting the 'with' block. Handles success or errors.
        :param exc_type: type of exception (if occurred)
        :param exc_val: exception message
        :param exc_tb: traceback
        :return: False to propagate the exception
        """
        if exc_type is None:
            # No errors occurred → delete the backup
            if os.path.exists(self.backup_filename):
                os.remove(self.backup_filename)
        else:
            # Error occurred → restore original file from backup
            if os.path.exists(self.backup_filename):
                with open(self.backup_filename, "r", encoding="utf-8") as f:
                    data = f.read()
                with open(self.filename, "w", encoding="utf-8") as f:
                    f.write(data)
                os.remove(self.backup_filename)
            print(f"An error occurred: {exc_val}. File restored from backup.")
        return False  # Do not suppress the exception


try:
    with BackupFile("important.txt") as f:
        # Work with the file
        with open(f, "w", encoding="utf-8") as file:
            file.write("New data")
        # Uncomment to test error handling
        # raise ValueError("Something went wrong!")
except Exception as e:
    print("File processing ended with an error.")
