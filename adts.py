"""
Basic Abstract data types : Stack, List, Queue and their
implementations at basic level
"""

__author__ = "Sadeeptha Bandara"

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')


class Stack(ABC, Generic[T]):
    """
     Pop
     Push
     Clear
     Is empty?
     Is full?
     length
    """
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """
        Add item to the top of the stack
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """
        Pop item from the top of the stack
        :return: Item
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """
        Peek at the item that is at the top of the stack
        :return:  Item
        """
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    def clear(self) -> None:
        """
        Clear stack
        """
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0


class Queue(ABC, Generic[T]):
    """
    Serve
    Append
    Clear
    Is empty?
    Is full?
    length
    """
    def __init__(self):
        self.length = 0

    @abstractmethod
    def serve(self) -> T:
        """
        Return the item at the start of the queue
        :return: Item
        """
        pass

    @abstractmethod
    def append(self, item: T) -> None:
        """
        Add new item to the end of the queue
        """
        pass

    @abstractmethod
    def is_full(self) -> bool:
        pass

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self) -> None:
        """
        Clears the queue
        """
        self.length = 0


class List(ABC, Generic[T]):
    """
    Getter
    Setter
    Insert at index, Append
    Find index
    Delete item at index
    Remove item
    Clear
    Is empty?
    Length
    """
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T):
        pass

    @abstractmethod
    def __getitem__(self, index: int):
        pass

    @abstractmethod
    def insert(self, item: T, index: int) -> None:
        """
        Insert provided item at specified index
        :param item: Item to be inserted
        :param index: Index at which to insert
        """
        pass

    @abstractmethod
    def append(self, item: T) -> None:
        """
        Insert item at the end of the list
        :param item: Item to be inserted
        """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """
        Will return the index of the first occurrence of a
        particular item within the list
        :param item: Item to find
        """
        pass

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """
        Delete an item at a provided index
        :param index: Index of item to be deleted
        """
        pass

    def remove(self, item: T) -> None:
        """
        Will remove the first occurrence of a particular item
        :param item: Item to remove
        """
        index = self.index(item)
        self.delete_at_index(index)

    def clear(self) -> None:
        self.length = 0

    def is_empty(self) -> bool:
        return len(self) == 0

    def __len__(self) -> int:
        return self.length


class SortedList(ABC, Generic[T]):
    def __init__(self):
        self.length = 0

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def add(self, item: T) -> None:
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        pass

    @abstractmethod
    def delete_at_index(self, index: int) -> None:
        pass

    def remove(self, item: T) -> None:
        index = self.index(item)
        self.delete_at_index(index)

    def __len__(self):
        return self.length

    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self.length = 0




