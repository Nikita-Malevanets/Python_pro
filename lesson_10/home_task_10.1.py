import re

pattern = r"^[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$"

print(bool(re.match(pattern, "example@domain.com")))
