"""
Basic Abstract data types : Stack, List, Queue and their
implementations at basic level
"""

__author__ = "Sadeeptha Bandara"

from abc import ABC, abstractmethod
from typing import TypeVar, Generic
T = TypeVar('T')


class Stack(ABC, Generic[T]):
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


class ArrayStack(Stack[T]):
    """
    Stack implementation with array.
    No resizing
    """
    DEFAULT_SIZE = 6

    def __init__(self, length: int = DEFAULT_SIZE) -> None:
        """
        complexity: O(n) where n is the length
        """
        Stack.__init__(self)
        self.array = [None] * length

    def push(self, item: T) -> None:
        """
        :complexity: O(1)
        """
        if self.is_full():
            raise IndexError("Stack is full. Pop or clear items to proceed")
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """
        complexity: O(1)
        """
        item = self.peek()
        self.length -= 1
        return item

    def peek(self) -> T:
        """
        :complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.array[len(self) - 1]

    def is_full(self) -> bool:
        """
        complexity: O(1)
        """
        return len(self.array) == len(self)


class LinearQueue(Queue[T]):
    """
    Queue implementation with array. Uses resizing.
    No circular implementation. Uses pointers to front and rear
    to avoid shifting elements
    """

    DEFAULT_CAPACITY = 6

    def __init__(self, length: int = DEFAULT_CAPACITY):
        """
        complexity: O(n)
        """
        Queue.__init__(self)
        self.front = 0
        self.rear = 0
        self.array = [None] * length

    def append(self, item: T) -> None:
        """
        :complexity: O(1)
        with resize O(n) where n is the size of the larger array
        """
        if self.is_full():
            self._resize()
        self.array[self.rear] = item
        self.rear += 1
        self.length += 1

    def serve(self) -> T:
        """
        :complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.array[self.front]
        self.front += 1
        self.length -= 1
        return item

    def _resize(self, factor: int = 2) -> None:
        """
        Creates new array with size larger than original, by the factor.
        Moves items over and resets pointers.
        :param factor: Factor by which array size is increased
        :complexity: O(n)
        """
        array = [None] * len(self.array) * factor
        ind = 0
        for i in range(self.front, self.rear):
            array[ind] = self.array[i]
            ind += 1
        self.front = 0
        self.rear = self.length
        self.array = array

    def is_full(self) -> bool:
        """
        :complexity: O(1)
        """
        return self.rear == len(self.array)

    def __str__(self):
        return_string = "["
        for i in range(self.front, self.rear):
            return_string += str(self.array[i]) + ", "
        return_string += "]"
        return return_string


class CircularQueue(Queue[T]):
    DEFAULT_CAPACITY = 6

    def __init__(self, length: int = DEFAULT_CAPACITY):
        self.front = 0
        self.rear = 0
        self.array = [None] * length

    def append(self, item: T) -> None:
        """
        :complexity: O(1)
        with resize O(n) where n is the size of the larger array
        """
        if self.is_full():
            self._resize()
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % len(self.array)
        self.length += 1

    def serve(self) -> T:
        """
        :complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.array[self.front]
        self.front = (self.front + 1) % len(self.array)
        self.length -= 1
        return item

    def _resize(self, factor: int = 2) -> None:
        """
        Creates new array with size larger than original, by the factor.
        Moves items over and resets pointers.
        :param factor: Factor by which array size is increased
        :complexity: O(n)
        """
        array = [None] * len(self.array) * factor
        ind = 0
        for i in range(self.front, self.rear):
            array[ind] = self.array[i]
            ind += 1
        self.front = 0
        self.rear = self.length
        self.array = array

    def is_full(self) -> bool:
        """
        :complexity: O(1)
        """
        return len(self) == len(self.array)

    def __str__(self):
        return_string = "["
        index = self.front
        for i in range(len(self)):
            return_string += str(self.array[index]) + ", "
            index = (index + 1) % len(self.array)
        return_string += "]"
        return return_string
