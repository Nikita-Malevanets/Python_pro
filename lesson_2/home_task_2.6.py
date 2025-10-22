from _ast import operator


def create_calculator(operator: str):
    """
    Create a simple calculator function based on the given operator.

    Parameters:
    operator (str): The operator for the calculation ('+', '-', '*', '/')

    Returns:
    function: A function that takes two numbers (a, b) and performs
              the chosen arithmetic operation.
              If division by zero occurs, it returns an error message.
    """

    # Define subtraction function
    def subtraction(a: int, b: int) -> int:
        return a - b

    # Define addition function
    def addition(a: int, b: int) -> int:
        return a + b

    # Define multiplication function
    def multiplication(a: int, b: int) -> int:
        return a * b

    # Define division function
    def division(a: int, b: int) -> float | str:
        if b == 0:
            return "you can't divide by zero"  # Handle division by zero
        return a / b

    # Return the corresponding function based on the operator
    if operator == '-':
        return subtraction
    elif operator == '+':
        return addition
    elif operator == '*':
        return multiplication
    elif operator == '/':
        return division
    else:
        # If operator is unknown, return a function that gives an error message
        return lambda a, b: "Unknown operator"


# --- Test ---
calc = create_calculator('/')
print(calc(5, 0))  # you can't divide by zero
print(calc(5, 2))  # 2.5

print(type(calc))
print(getattr(calc, '__name__'))
print(calc.__name__)
print(calc.__doc__)
print()
