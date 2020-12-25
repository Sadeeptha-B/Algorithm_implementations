"""
Linked Node implementations of ADTs.

"""

__author__ = "Sadeeptha Bandara"

from typing import Generic, TypeVar
from adts import List

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.next = None

    def set_item(self, item: T) -> None:
        self.item = item

    def __str__(self):
        return str(self.item)


class LinkedList(List, Generic[T]):
    def __init__(self):
        List.__init__(self)
        self.head = None

    def insert(self, item: T, index: int) -> None:
        if index == 0:
            temp = self.head
            self.head = Node(item)
            self.head.next = temp
        else:
            parent = self._goto_parent(index)
            temp = parent.next
            parent.next = Node(item)
            parent.next.next = temp
        self.length += 1

    def append(self, item: T) -> None:
        if self.is_empty():
            self.head = Node(item)
        else:
            parent = self._go_to_final_elem()
            parent.next = Node(item)
        self.length += 1

    def __setitem__(self, index: int, item: T) -> None:
        if index >= len(self):
            raise IndexError("Index is out of bounds")

        if index == 0:
            temp = self.head.next
            self.head = Node(item)
            self.head.next = temp
        else:
            parent = self._goto_parent(index)
            temp = parent.next.next
            parent.next = Node(item)
            parent.next.next = temp

    def __getitem__(self, index: int) -> T:
        if index >= len(self):
            raise IndexError("Index is out of bounds")

        if index == 0:
            return self.head.item
        else:
            parent = self._goto_parent(index)
            return parent.next.item

    def delete_at_index(self, index: int) -> T:
        if index >= len(self):
            raise IndexError("Index is out of bounds")

        if index == 0:
            self.head = self.head.next
        else:
            parent = self._goto_parent(index)
            parent.next = parent.next.next

    def _goto_parent(self, index: int) -> T:
        if index >= len(self):
            raise IndexError("Index is out of bounds")

        if index == 0:
            raise ValueError("Index 0 has no parent")

        current = self.head
        for _ in range(index - 1):
            current = current.next
        return current

    def _go_to_final_elem(self):
        if self.is_empty():
            raise ValueError("List is empty")

        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def index(self, item: T) -> int:
        index = 0
        current = self.head
        while current is not None:
            if current.item == item:
                return index
            current = current.next
            index += 1
        raise KeyError("Item not found")

    def __str__(self):
        return_string = "["
        current = self.head
        while current is not None:
            return_string += str(current) + ", "
            current = current.next
        return_string += "]"
        return return_string


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.insert(11, 0)
    print(my_list)
    items = [4, 6, 2, 10, 3, 7, 8]
    for item in items:
        my_list.append(item)
    print(my_list)

    my_list.remove(4)
    print(my_list)
    print(my_list.index(8))
    try:
        print(my_list.index(4))
    except KeyError:
        print("Not found")

    my_list.insert(4, 2)
    print(my_list)
    my_list.insert(11, 0)
    print(my_list)
