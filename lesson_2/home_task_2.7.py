# Global variable to store total expenses
total_expense : float = 2.0


def add_expense() -> None:
    """
        Ask the user to input an expense and add it to total_expense.
        Handles invalid input by showing a message.
        """
    global total_expense
    try:
        your_expense :float = float(input("Add your expense: "))
        total_expense += your_expense
        print(f'Added {your_expense} to total expenses')
    except ValueError:
        print("Invalid input. Please enter a number.")


def get_expense() -> None:
    """
        Return the current total expenses
        """
    print(f"Total expenses: {total_expense}")


# Ask user what they want to do
work_with_expense : str = input("If you want add expense enter: 'add', if you want check balance enter: 'check' ")

# Perform the chosen action
if work_with_expense == 'add':
    add_expense()
elif work_with_expense == 'check':
    get_expense()
else:
    print("Invalid input")

# Show final total expenses
print(f'Total expenses are {total_expense} now.')
