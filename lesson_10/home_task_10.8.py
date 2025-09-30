import re


def remove_urls(input_text: str) -> str:
    """
        Remove all URLs from the input text.

        Args:
            input_text (str): Text containing URLs.

        Returns:
            str: Text without URLs.
        """
    pattern = r'https?://[^\s]+\.[a-z]{2,4}|www\.[^\s]+\.[a-z]{2,4}'
    return re.sub(pattern, '', input_text)


text = "Check this site: https://example.com and also visit www.test.org or http://hello.net our web site"
print(remove_urls(text))
