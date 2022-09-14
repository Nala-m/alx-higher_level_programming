#!/usr/bin/python3
python3 - c 'print(__import__("my_module").__doc__)'


class Square:
    python3 - c 'print(__import__("my_module").MyClass.__doc__)'
    python3 - c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """Class Square that defines a square object
    """
    def __init__(self, size):
        """Initialize method that stores the size of the square
        Args:
            param1 (int): size of the square
        """
        self.__size = size
