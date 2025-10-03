import csv
import os

from PIL import Image


def collect_image_stats(folder_path, output_csv):
    """
    Collects basic metadata (filename, format, width, height) from all images
    in a specified folder and saves it to a CSV file.

    Args:
        folder_path (str): Path to the folder containing images.
        output_csv (str): Name of the CSV file to save the metadata.

    Steps:
        1. List all files in the folder using os.listdir().
        2. Filter only image files by extensions (.jpg, .png, .jpeg, .bmp).
        3. Create a CSV file and write headers (filename, format, width, height).
        4. Open each image using PIL.Image.open() and extract metadata.
        5. Write metadata of each image as a row in the CSV file.

    Example:
        collect_image_stats("images", "image_stats.csv")
    """
    # 1. List all files in the folder
    files = os.listdir(folder_path)

    # 2. Filter only image files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    # 3. Create CSV file and write headers
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["filename", "format", "width", "height"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 4. Open each image and write metadata
        for file_name in image_files:
            file_path = os.path.join(folder_path, file_name)  # full path to the file
            with Image.open(file_path) as img:  # open image
                writer.writerow({  # write one row per image
                    "filename": file_name,
                    "format": img.format,
                    "width": img.size[0],
                    "height": img.size[1]
                })


# Example usage
collect_image_stats("images", "image_stats.csv")
