import os
import zipfile


class ZipArchive:
    """
    Context manager for creating and managing a ZIP archive.

    Usage:
        with ZipArchive("archive.zip") as archive:
            archive.add_file("file1.txt")
            archive.add_file("file2.txt")
    """

    def __init__(self, archive_name):
        self.archive_name = archive_name
        self.zip_file = None  # placeholder for the ZipFile object

    def __enter__(self):
        # Open the ZIP archive in write mode with compression
        self.zip_file = zipfile.ZipFile(
            self.archive_name, "w", zipfile.ZIP_DEFLATED
        )
        return self  # return the object so we can call add_file()

    def add_file(self, filename, arcname=None):
        # Add file if it exists
        if os.path.exists(filename):
            self.zip_file.write(filename, arcname or filename)
            print(f"Added: {filename}")
        else:
            print(f"Skipped: {filename} (not found)")

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Safely close the archive
        if self.zip_file:
            self.zip_file.close()
            print(f"Archive '{self.archive_name}' closed.")

        # If an error happened — print it (but do not suppress the exception)
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False  # Allow exceptions to propagate if needed


try:
    with ZipArchive("my_files.zip") as archive:
        archive.add_file("important.txt")
        archive.add_file("data.csv")
        archive.add_file("missing_file.txt")  # This will be skipped
except Exception as e:
    print("Something went wrong!")
