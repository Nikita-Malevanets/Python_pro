import re


def searching_all_ip(input_text: str) -> list[str]:
    """
    Extract all valid IPv4 addresses from the given text.

    An IPv4 address consists of four numbers (0–255) separated by dots.
    The function uses a regular expression to validate each number and
    returns only valid IP addresses.

    Args:
        input_text (str): The input text that may contain IP addresses.

    Returns:
        list[str]: A list of all valid IPv4 addresses found in the text.
    """
    pattern = (
        r"\b"
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
        r"(?:[0-9]{1,2}|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
        r"\b"
    )
    return re.findall(pattern, input_text)


text = "servers: 192.168.1.1, 10.0.0.255 и 256.100.50.25 ."
print(searching_all_ip(text))
