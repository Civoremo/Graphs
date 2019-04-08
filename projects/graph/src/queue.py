# import sys
# sys.path.append('../linked_list')

from linked_list import LinkedList
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = LinkedList()
        # self.storage = DoublyLinkedList()

    def enqueue(self, item):
        # pass
        self.storage.add_to_tail(item)
        self.size += 1

    def dequeue(self):
        # pass
        if self.size > 0:
            old_head_value = self.storage.remove_from_head()
            self.size -= 1
            return old_head_value

    def len(self):
        # pass
        return self.size
