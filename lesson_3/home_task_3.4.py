class BinaryNumber:
    """
    A class to represent a binary number and do binary operations.
    """

    def __init__(self, value: int) -> None:
        """
        Make a new binary number.

        Parameters:
        value (int): The number to represent in binary.
        """
        self.value = value

    def __and__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Bitwise AND with another binary number.

        Parameters:
        other (BinaryNumber): Another number.

        Returns:
        BinaryNumber: Result of AND operation.
        """
        return BinaryNumber(self.value & other.value)

    def __or__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Bitwise OR with another binary number.

        Parameters:
        other (BinaryNumber): Another number.

        Returns:
        BinaryNumber: Result of OR operation.
        """
        return BinaryNumber(self.value | other.value)

    def __xor__(self, other: "BinaryNumber") -> "BinaryNumber":
        """
        Bitwise XOR with another binary number.

        Parameters:
        other (BinaryNumber): Another number.

        Returns:
        BinaryNumber: Result of XOR operation.
        """
        return BinaryNumber(self.value ^ other.value)

    def __invert__(self) -> "BinaryNumber":
        """
        Bitwise NOT (invert) the binary number.

        Returns:
        BinaryNumber: Result of NOT operation (8 bits).
        """
        return BinaryNumber(~self.value & 0xFF)

    def __repr__(self) -> str:
        """
        Show the binary number as text.

        Returns:
        str: Binary string (8 bits).
        """
        return bin(self.value)[2:].zfill(8)


a = BinaryNumber(0b10101010)
b = BinaryNumber(0b11001100)

print("a =", a)
print("b =", b)
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
