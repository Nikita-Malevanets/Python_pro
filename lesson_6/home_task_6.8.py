import json


class ConfigManager:
    """
    Simple context manager for working with JSON configuration files.

    When entering the context:
        - Load configuration from file, or use empty dict if file doesn't exist.
    When exiting the context:
        - Save configuration back to the file.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def __enter__(self):
        # Try to read the file
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)
        except FileNotFoundError:
            self.config = {}  # Start with empty settings if file doesn't exist
        return self.config  # This will be assigned to "as config"

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always write config back to file when exiting
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)
        return False  # Don't ignore possible exceptions


with ConfigManager("config.json") as config:
    config["theme"] = "dark"
    config["volume"] = 75

print(config)
