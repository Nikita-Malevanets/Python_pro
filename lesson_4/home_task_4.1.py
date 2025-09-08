class UnknownOperationError(Exception):
    """Custom exception for unknown arithmetic operations."""
    pass


class Calculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, first_number, second_number):
        """Returns the sum of two numbers."""
        return first_number + second_number

    def subtract(self, first_number, second_number):
        """Returns the difference between two numbers."""
        return first_number - second_number

    def multiply(self, first_number, second_number):
        """Returns the product of two numbers."""
        return first_number * second_number

    def divide(self, first_number, second_number):
        """Returns the division of two numbers. Raises ZeroDivisionError if denominator is zero."""
        if second_number == 0:
            raise ZeroDivisionError("Division by zero is not allowed!")
        return first_number / second_number

    def calculate(self, first_number: float, operation: str, second_number: float):
        """
        Performs the specified arithmetic operation on two numbers.
        Raises UnknownOperationError for unsupported operations.
        Raises OverflowError if the result exceeds float limits.
        """
        if operation == "+":
            result = self.add(first_number, second_number)
        elif operation == "-":
            result = self.subtract(first_number, second_number)
        elif operation == "*":
            result = self.multiply(first_number, second_number)
        elif operation == "/":
            result = self.divide(first_number, second_number)
        else:
            raise UnknownOperationError(f"Unknown operation: {operation}")

        # Check for overflow (extremely large result)
        if abs(result) > 1e308:
            raise OverflowError("Result is too large!")

        return result


# This block runs only when the file is executed directly
if __name__ == "__main__":
    calculator = Calculator()
    try:
        # Read input from user
        first_number = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        second_number = float(input("Enter the second number: "))

        # Perform calculation
        result = calculator.calculate(first_number, operation, second_number)

        # Display result with 2 decimal places
        print(f"Result: {result:.2f}")

    except ValueError:
        print("Error: Invalid number entered.")
    except ZeroDivisionError as error:
        print(f"Error: {error}")
    except UnknownOperationError as error:
        print(f"Error: {error}")
    except OverflowError as error:
        print(f"Error: {error}")
