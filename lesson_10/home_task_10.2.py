import re


def searching_tel_numbers(input_text):
    pattern = r"\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}"
    return re.findall(pattern, input_text)


text = "Call me at (123) 456-7890 or 987-654-3210 or 123.456.7890 or 1234567890."

print(searching_tel_numbers(text))
