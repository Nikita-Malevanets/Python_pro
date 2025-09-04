class Person:
    """
    A class to represent a person with name and age.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Make a new person.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.

        Returns:
        None
        """
        self.name = name
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """
        Check if this person is younger than another.

        Parameters:
        other (Person): Another person.

        Returns:
        bool: True if this person is younger.
        """
        return self.age < other.age

    def __eq__(self, other: "Person") -> bool:
        """
        Check if this person has the same age as another.

        Parameters:
        other (Person): Another person.

        Returns:
        bool: True if ages are equal.
        """
        return self.age == other.age

    def __gt__(self, other: "Person") -> bool:
        """
        Check if this person is older than another.

        Parameters:
        other (Person): Another person.

        Returns:
        bool: True if this person is older.
        """
        return self.age > other.age

    def __repr__(self) -> str:
        """
        Show the person in text form .

        Returns:
        str: Name and age of the person.
        """
        return f"{self.name} ({self.age})"
