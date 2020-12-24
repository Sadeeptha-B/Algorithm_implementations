"""
Array implementations of ADTs
Contains
- Lists, Queues, Stacks
"""

__author__ = "Sadeeptha Bandara"

from typing import TypeVar
from adts import Stack, Queue, List, SortedList
T = TypeVar('T')


# ArrayStack
# =================================================================
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


# Queue : Linear
# ==============================================================
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

    def clear(self) -> None:
        Queue.clear(self)
        self.front = 0
        self.rear = 0


# Queue: Circular
# ==================================================================
class CircularQueue(Queue[T]):
    DEFAULT_CAPACITY = 6

    def __init__(self, length: int = DEFAULT_CAPACITY):
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
        index = self.front
        for i in range(len(self)):
            array[i] = self.array[index]
            index = (index + 1) % len(self.array)
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

    def clear(self) -> None:
        Queue.clear(self)
        self.front = 0
        self.rear = 0


class ArrayList(List[T]):
    DEFAULT_LENGTH = 6

    def __init__(self, length: int = DEFAULT_LENGTH):
        List.__init__(self)
        self.array = [None] * length

    def __setitem__(self, index: int, item: T):
        """
        :complexity: O(1)
        """
        if index >= len(self):
            raise IndexError("Index is out of bounds")
        self.array[index] = item

    def __getitem__(self, index: int):
        """
        :complexity: O(1)
        """
        if index >= len(self):
            raise IndexError("Index is out of bounds")
        return self.array[index]

    # IMPROVE
    def insert(self, index: int, item: T) -> None:
        """
        Insert item at specified index
        :complexity: O(n)
        """
        if len(self) == len(self.array):
            self._resize()

        array = [None] * (len(self) - index)
        ind = 0
        for i in range(index, len(self)):
            array[ind] = self.array[i]
            ind += 1

        ind = 0
        for i in range(index + 1, len(self) + 1):
            self.array[i] = array[ind]
            ind += 1

        self.array[index] = item
        self.length += 1

    def append(self, item: T) -> None:
        if len(self) == len(self.array):
            self._resize()
        self.array[len(self)] = item
        self.length += 1

    def _resize(self, factor: int = 2):
        array = [None] * len(self.array) * factor
        for i in range(len(self)):
            array[i] = self.array[i]
        self.array = array

    def index(self, item: T) -> int:
        for i in range(len(self)):
            if self.array[i] == item:
                return i
        raise KeyError("Item not found")

    def delete_at_index(self, index: int) -> T:
        for i in range(index, len(self)):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def __str__(self):
        return_string = "["
        for i in range(len(self)):
            return_string += str(self.array[i]) + ", "
        return_string += "]"
        return return_string


class SortedArrayList(SortedList):
    DEFAULT_SIZE = 6

    def __init__(self, size: int = DEFAULT_SIZE):
        SortedList.__init__(self)
        self.array = [None] * size

    def __getitem__(self, index: int):
        if index >= len(self):
            raise IndexError("Index is out of bounds")
        return self.array[index]

    def index(self, item: T) -> int:
        low = 0
        high = len(self) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == item:
                return mid
            elif self.array[mid] > item:
                high = mid - 1
            elif self.array[mid] < item:
                low = mid + 1
        raise KeyError("Item not found")

    def delete_at_index(self, index: int) -> None:
        for i in range(index, len(self)):
            self.array[i] = self.array[i+1]
        self.length -= 1

    def add(self, item: T) -> None:
        if len(self) == len(self.array):
            self._resize()

        self.array[len(self)] = item
        for i in range(len(self) - 1, -1, -1):
            if item < self.array[i]:
                self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
        self.length += 1

    def _resize(self, factor: int = 2):
        array = [None] * len(self.array) * factor
        for i in range(len(self)):
            array[i] = self.array[i]
        self.array = array

    def __str__(self):
        return_string = "["
        for i in range(len(self)):
            return_string += str(self.array[i]) + ", "
        return_string += "]"
        return return_string


if __name__ == "__main__":
    my_list = SortedArrayList()
    items = [4, 6, 2, 10, 3, 7, 8]
    for item in items:
        my_list.add(item)
    print(my_list)
    my_list.remove(4)
    print(my_list)
    print(my_list.index(8))
    try:
        print(my_list.index(4))
    except KeyError:
        print("Not found")






