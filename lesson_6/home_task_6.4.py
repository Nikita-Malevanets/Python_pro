def filter_lines_safe(filename, search_keyword):
    """
    Generator that yields lines from a file containing a specific keyword.

    Args:
        filename (str): Path to the text file.
        search_keyword (str): Keyword to search in each line.

    Yields:
        str: Lines that contain the keyword.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file_handle:
            for current_line in file_handle:
                if search_keyword in current_line:
                    yield current_line.rstrip("\n")
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return


# Example usage
input_file = "big_log.txt"
output_file = "filtered_log.txt"
keyword_to_search = "ERROR"

with open(output_file, "w", encoding="utf-8") as out_file:
    for matched_line in filter_lines_safe(input_file, keyword_to_search):
        out_file.write(matched_line + "\n")
        print(matched_line)
