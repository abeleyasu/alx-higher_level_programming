README
This repository contains a Python script that defines a function to print a specified number of elements from a list. The function is designed to handle various data types within the list and provides the flexibility to print a number of elements that may exceed the length of the list.
Function Description
The function is defined as follows:
python
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list
    :param my_list: the list to print elements from
    :param x: the number of elements to print
    :return: the real number of elements printed
    """
    # Function implementation

my_list: Can contain any type (integer, string, etc.).
x: Represents the number of elements to print. It can be bigger than the length of my_list.
The function returns the real number of elements printed.
It uses try and except to handle exceptions.
It does not import any module and does not use len().
Example Usage
python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))  # Output: 12
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))  # Output: 12345
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))  # Output: 12345

How to Use
To use the function, simply import it into your Python script and call it with the appropriate parameters.
python
from safe_print_list import safe_print_list

# Define your list
my_list = [1, 2, 3, 4, 5]

# Call the function with the desired number of elements to print
nb_print = safe_print_list(my_list, 3)
print("Number of elements printed: {:d}".format(nb_print))

Repository Information
GitHub Repository: 0x05-python-exceptions
Feel free to use this function in your Python projects. If you have any feedback or suggestions, please feel free to open an issue or a pull request.
