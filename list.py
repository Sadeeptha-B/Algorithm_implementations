class LinkedList:
    def __init__(self):
        self.head = Node()

    def insert(self, node):
        current = self.head
        while current.link is not None:
            current = current.link
        current.link = node

    def __len__(self):
        return self.__len_aux(self.head)

    def __len_aux(self, current):
        if current is None:
            return -1
        else:
            return 1 + self.__len_aux(current.link)

    def is_empty(self):
        return len(self) == 0

    def __delitem__(self, key):
        current = self.head
        while current.link is not None:
            if current.link == key:
                current.link = current.link.link
                break

    def __contains__(self, item):
        return self.__contains_aux(self.head, item)

    def __contains_aux(self, current, item):
        if current is None:
            return False
        if current == item:
            return True
        return self.__contains_aux(current.link, item)
        # return current == item or self.__contains_aux(current.link, item)
        # However, this will not treat finding the element as a base case.

    def get_root(self):
        return self.head

class Node:
    def __init__(self, node_id=None):
        self.id = node_id
        self.link = None

    def set_link(self, node):
        self.link = node()


def sum_queue(queue):
    return __sum_queue_aux(queue, queue.get_root().link)


def __sum_queue_aux(queue, current):
    if queue.is_empty():
        return 0
    id = current.id
    link = current.link
    del queue[current]      # serving is a better way to do this
    return id + __sum_queue_aux(queue, link)


if __name__ == "__main__":
    linked_list = LinkedList()
    elems = [3, 4, 5, 6]
    nodes = [None] * 4
    for i in range(len(elems)):
        nodes[i] = Node(elems[i])

    for node in nodes:
        linked_list.insert(node)

    print(linked_list.__contains__(nodes[3]))
    print(linked_list.__contains__(Node()))
    print(len(linked_list))

    print(sum_queue(linked_list))