#!/usr/bin/python3
"""This module defines a Node class and a SinglyLinkedList class."""


class Node:
    """This class represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new instance of the Node class.

        Args:
            data: The data to be stored in the node.
            next_node: The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data attribute.

        Args:
            value: The new value for the data attribute.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node attribute.

        Args:
            value: The new value for the next_node attribute.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class represents a singly linked list."""

    def __init__(self):
        """Initialize a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order).

        Args:
            value: The data for the new Node.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result


# Test cases
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

