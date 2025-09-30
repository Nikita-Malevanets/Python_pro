import re


def searching_hash_tags(input_text):
    pattern = r"#\w+"
    return re.findall(pattern, input_text)


text = "I love #Python and #100DaysOfCode but not #fun-time or #hello!"

print(searching_hash_tags(text))
