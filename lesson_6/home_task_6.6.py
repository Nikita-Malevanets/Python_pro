import os


def iterate_image_files(folder_path):
    """
    A generator that yields all image files in a given folder one by one.
    For each image, it returns its name, size in bytes, and full path.

    Args:
        folder_path (str): Path to the folder to iterate through.

    Yields:
        tuple: (file_name, file_size, full_path)

    Example:
        for name, size, path in iterate_image_files("images"):
            print(name, size, path)
    """
    # Allowed image extensions
    allowed_extensions = ('.jpg', '.jpeg', '.png', '.bmp')

    # List all items in the folder
    for file_name in os.listdir(folder_path):
        # Build full path to the file
        file_path = os.path.join(folder_path, file_name)

        # Check if it is a file and has allowed image extension
        if os.path.isfile(file_path) and file_name.lower().endswith(allowed_extensions):
            # Get file size in bytes
            file_size = os.path.getsize(file_path)
            # Return name, size, and path
            yield file_name, file_size, file_path


# Example usage
folder_path = "images"  # change to your folder
for name, size, path in iterate_image_files(folder_path):
    print(f"File: {name}, Size: {size} bytes, Full path: {path}")
