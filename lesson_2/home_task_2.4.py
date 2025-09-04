default_time = 60  # Global default time per training round (in minutes)


def training_session(rounds: int):
    # Initialize the time per round using the global default
    time_per_round = default_time

    def adjust_time(delta):
        # Allows the inner function to modify time_per_round from the enclosing scope
        nonlocal time_per_round
        # Adjust the time for the next round
        time_per_round += delta

    # Loop through each training round
    for round_number in range(1, rounds + 1):
        # Print the current round and its duration
        print(f'Round {round_number}: {time_per_round} minutes')
        # Adjust the time for the next round, except after the last round
        if round_number < rounds:
            adjust_time(-5)


# Example usage
training_session(3)
