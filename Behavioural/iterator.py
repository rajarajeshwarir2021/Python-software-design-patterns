"""
ITERATOR
A way to traverse through a collection and apply some functionality or return it
* Implements two methods:
    - has_next
    - next
"""


class AlphabeticalOrderIterator:
    """Alphabetical Order Iterator class"""
    def __init__(self, words, reverse: bool = False):
        self.collection = sorted(words)
        self.reverse = reverse
        self.position = len(words) - 1 if reverse else 0

    def next(self):
        """Next method"""
        value = self.collection[self.position]
        self.position += -1 if self.reverse else 1
        return value

    def has_next(self):
        """Has Next method"""
        if self.reverse and self.position > -1:
            return True
        elif not self.reverse and self.position < len(self.collection):
            return True
        else:
            return False


class WordsCollection:
    """Words Collection method"""
    def __init__(self, collection):
        self.collection = collection

    def get_iterator(self):
        """Get iterator method"""
        return AlphabeticalOrderIterator(self.collection)

    def get_reverse_iterator(self):
        """Get reverse iterator"""
        return AlphabeticalOrderIterator(self.collection, True)


if __name__ == '__main__':
    # Iterator
    collection = WordsCollection(["Bob", "Alice", "Florian", "Margaret"])
    iterator = collection.get_iterator()
    reverse_iterator = collection.get_reverse_iterator()

    # Print iterator
    while iterator.has_next():
        print(iterator.next())

    print()

    # Print reverse iterator
    while reverse_iterator.has_next():
        print(reverse_iterator.next())
