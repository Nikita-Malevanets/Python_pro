import re


def searching_all_dates(input_text):
    """
       Convert all dates in a text from DD/MM/YYYY format to YYYY-MM-DD format.

       Parameters:
       input_text (str): The text containing dates in DD/MM/YYYY format.

       Returns:
       str: A new string with all dates converted to YYYY-MM-DD format.
       """
    pattern = r"(\d{2})/(\d{2})/(\d{4})"

    def reformat_dates(match):
        day = int(match.group(1))
        month = int(match.group(2))
        year = int(match.group(3))
        return f"{year}-{month}-{day}"

    return re.sub(pattern, reformat_dates, input_text)


text = "Today is 31/12/2023 and tomorrow will be 01/01/2024."

print(searching_all_dates(text))
