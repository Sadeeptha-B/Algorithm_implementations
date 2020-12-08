__author__ = "Sadeeptha Bandara"


class Trie:
    def __init__(self, init_words):
        self.root = Node()
        for word in init_words:
            self.insert(word)

    def insert(self, word: str):
        current = self.root
        for letter in word:
            index = ord(letter) - 96
            if current.link[index] is None:
                current.link[index] = Node()
            current = current.link[index]
        current.link[0] = Node()

    def search(self, word: str):
        current = self.root
        for letter in word:
            index = ord(letter) - 96
            if current.link[index] is None:
                return False
            current = current.link[index]
        return current.link[0] is None

    def inorder_traversal(self, source):
        pass

    def __str__(self):
        current = self.root
        pass


class Node:
    ALPHABET_SIZE = 27

    def __init__(self):
        self.link = [None] * Node.ALPHABET_SIZE


if __name__ == "__main__":
    trie_words = ["taco", "taro", "tarot", "coco", "chobo"]
    new_Trie = Trie(trie_words)