def create_user_settings():
    """
    Create a closure to store and manage user settings.
    Returns a function that can get or update settings.
    """
    # Dictionary to store user settings
    settings = {
        "theme": "light",
        "language": "en",
        "notifications": True
    }

    # Inner function to get or update a setting
    def user_settings(key: str, new_value=None):
        # Check if the setting exists
        if key not in settings:
            return "Setting not found"

        # Update the setting if a new value is provided
        if new_value is not None:
            settings[key] = new_value
            return f"{key} updated to {new_value}"

        # Return the current value if no new value is provided
        return settings[key]

    return user_settings  # Return the inner function
