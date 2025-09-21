class User:
    """
    User class with attributes first_name, last_name, and email.
    Provides validation using @property and setter methods.
    """

    def __init__(self, first_name, last_name, email):
        """
        Initialize a User object with first_name, last_name, and email.
        Setter methods are used to validate the input values.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        """Get the first name of the user."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """Set the first name with validation."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError('First name must be a non-empty string!')
        self._first_name = value

    @property
    def last_name(self):
        """Get the last name of the user."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """Set the last name with validation."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Last name must be a non-empty string!')
        self._last_name = value

    @property
    def email(self):
        """Get the email of the user."""
        return self._email

    @email.setter
    def email(self, value):
        """Set the email with validation."""
        if '@' not in value or '.' not in value:
            raise ValueError('Email must be a valid email address!')
        self._email = value
