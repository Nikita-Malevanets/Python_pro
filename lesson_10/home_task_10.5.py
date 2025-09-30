import re


def remove_html_tags(input_text: str) -> str:
    """
        Remove all HTML tags from the given text.

        Parameters:
        input_text (str): A string that may contain HTML tags.

        Returns:
        str: Text with all HTML tags removed.
        """
    return re.sub(r'<.*?>', '', input_text)


text = "<p>Hello <b>world</b>! This is <a href='#'>a link</a>.</p>"

print(remove_html_tags(text))
