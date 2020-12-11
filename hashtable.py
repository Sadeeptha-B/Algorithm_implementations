"""
HashTable implementations
"""

__author__ = "Sadeeptha Bandara"

class HashTable:
    """
    HashTable that makes use of cuckoo hashing
    """
    DEFAULT_TBL_SIZES = [13, 7]
    DEFAULT_KICK_LIMIT = 10

    def __init__(self, size_tbl_one=DEFAULT_TBL_SIZES[0], size_tbl_two=DEFAULT_TBL_SIZES[1]):
        """
        Initializes two tables and stores in a table array
        :param size_tbl_one: Table_one size
        :param size_tbl_two: Table_two size
        """
        self.table_one = [None] * size_tbl_one
        self.table_two = [None] * size_tbl_two
        self.cuckoo_limit = HashTable.DEFAULT_KICK_LIMIT
        self.table_array = [self.table_one, self.table_two]

    def hash(self, key, table):
        """
        Will hash provided key into a provided table
        :return: Will return hashed index to relevant table
        """
        if self.table_array.count(table) < 0:
            raise ValueError("Invalid table")
        key = int(key)
        hash = key % len(table)
        return hash

    def insert(self, elem):
        """
        Inserts provided element, bu hashing based on key
        :param elem: Element to be inserted. Will need to be provided in the form of a two element
                    tuple in the form of (key, item)
        :complexity: O(1) in general
                      O(N) resizing
        """
        prev_elem = self.__insert_to_table(elem, self.table_one)
        kick_count = 1
        table_ind = 1
        while prev_elem is not None:
            prev_elem = self.__insert_to_table(prev_elem, self.table_array[table_ind])
            table_ind = (table_ind + 1) % len(self.table_array)
            kick_count += 1
            if kick_count >= self.cuckoo_limit:
                break
                self.resize()

    def __insert_to_table(self, elem, table):
        """
        Provided an element and a table to insert in, will insert and return
        the previously occupied element at the hashed index
        :param elem: Element to be inserted. Must be in the form of a two element tuple
                    in the form of (key, item)
        :param table: Table to insert element in
        :return: Returns element that previously occupied hash index and None if no element did.
        """
        key, item = elem
        hash_ind = self.hash(key, table)
        prev_elem = table[hash_ind]
        table[hash_ind] = elem
        return prev_elem

    def __search(self, key):
        """
        Will search for an item if key exists
        :return: If item is found, will return item, else will raise a KeyError
        """
        for table in self.table_array:
            hash_ind = self.hash(key, table)
            elem = table[hash_ind]
            if elem is not None:
                found = elem[0] == key
                if found:
                    return elem[1]
        raise KeyError("Item not found")

    def __getitem__(self, key):
        """
        Search item will handle for KeyError
        :return: Will return item or error message
        """
        try:
            item = self.__search(key)
            return item
        except KeyError as e:
            return e.__str__()

    def resize(self, *tables):
        """
        Will resize provided tables
        :param tables: Tables to be resized.
        """
        for table in tables:
            if self.table_array.count(table) < 0:
                raise ValueError("Invalid table")

    def set_kick_limit(self, kick_limit):
        """Set appropriate kick limit. Overrides default"""
        self.cuckoo_limit = kick_limit

    def __str__(self):
        """
        String representation of insertions.
        """
        return_string = ""
        for table in self.table_array:
            return_string += "["
            for elem in table:
                return_string += elem.__str__() + ", "
            return_string += "]"
        return return_string


if __name__ == "__main__":
    hashtable = HashTable()
    insert_elems = [(23, "a"), (36, "b"), (114, "c"), (49, "d")]
    for elem in insert_elems:
        hashtable.insert(elem)
    for elem in insert_elems:
        key = elem[0]
        print(hashtable[key])
    print(hashtable)





