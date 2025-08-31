def my_sum() -> str:
    """Custom function which we will use instead of built-in 'sum'."""
    return "This is my custom sum function!"


list_of_numbers = [2, 2, 2]

print(sum(list_of_numbers)) # We try to use built-in sum
print(my_sum())  # Showing functionality of function

sum = my_sum  # Shadowing built-in 'sum'


print(sum(list_of_numbers)) # Will be error, because 'sum' working not correct now
