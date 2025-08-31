subscribers = []  # Global list to store subscriber names


def subscribe(name: str) -> str:
    """
    Add a new subscriber to the global list.

    Args:
        name (str): The name of the subscriber to add.

    Returns:
        A nested function that, when called, confirms the subscription.
    """
    subscribers.append(name)  # Adding name to global list

    def confirm_subscription():
        """Return confirmation message for the subscriber."""
        return f'Subscription is approved for {name}'

    return confirm_subscription()  #


def unsubscribe(name: str) -> str:
    """
    Remove a subscriber from the global list.

    Args:
        name (str): The name of the subscriber to remove.

    Returns:
        str: Confirmation message or error if subscriber not found.
    """
    if name in subscribers:
        subscribers.remove(name)
        return f'{name} has been removed successfully from subscription'
    else:
        return f'Name {name} not found'


subscribe("Olena")  # Subscription confirmed for Olena
subscribe("Ihor")  # Subscription confirmed for Ihor

print(subscribers)  # ['Olena', 'Ihor']
print(unsubscribe("Ihor"))  # 'Ihor has been removed'
print(subscribers)  # ['Olena']
