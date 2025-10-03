def error_lines_from_log(log_file, output_file):
    """
    A generator that reads a large log file line by line and returns only
    the lines containing HTTP error status codes (4XX or 5XX).
    It also writes these lines into a separate file for analysis.

    Args:
        log_file (str): Path to the large log file.
        output_file (str): Path to save the extracted error lines.

    Yields:
        str: Each line containing an HTTP error code (4XX or 5XX).

    Example:
        for line in error_lines_from_log("server.log", "errors.log"):
            print(line)
    """
    with open(log_file, "r", encoding="utf-8") as f, \
            open(output_file, "w", encoding="utf-8") as out_f:
        for line in f:  # read the file line by line
            # Simple check: look for 4XX or 5XX status in the line
            # Here we assume the status code is a separate word in the line
            words = line.split()
            for word in words:
                if word.startswith("4") or word.startswith("5"):
                    if word.isdigit() and len(word) == 3:  # check it's a proper HTTP code
                        out_f.write(line)  # save to output file
                        yield line  # return this line from generator
                        break  # no need to check other words in this line
