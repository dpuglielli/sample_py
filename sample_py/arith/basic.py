"""Module for basic arithmetic
"""


class Basic:
    """Class for basic arithmetic"""

    def add(self, val1, val2):
        """Basic adder

        Args:
            val1 (float): value 1
            val2 (float): value 2

        Returns:
            float: sum of val and val2
        """
        result = val1 + val2
        return result

    def subtract(self, val1, val2):
        """Basic subtraction

        Args:
            val1 (float): value 1
            val2 (float): value 2

        Returns:
            float: result of val - val2
        """
        result = val1 - val2
        return result

    def multiply(self, val1, val2):
        """Basic multiplication

        Args:
            val1 (float): value 1
            val2 (float): value 2

        Returns:
            float: result of val * val2
        """
        result = val1 * val2
        return result

    def divide(self, val1, val2):
        """Basic division

        Args:
            val1 (float): value 1
            val2 (float): value 2

        Returns:
            float: result of val / val2
        """
        result = val1 / val2
        return result
