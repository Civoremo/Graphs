class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_from_head(self):
        if not self.head and not self.tail:
            return None

        old_head_value = self.head.value

        if self.head is self.tail:
            self.head = None
            self.tail = None
            return old_head_value
        else:
            self.head = self.head.get_next()
            return old_head_value

    def contains(self, target):
        if not self.head and not self.tail:
            return False

        current = self.head

        while current:
            if current.value == target:
                return True

            current = current.get_next()
        return False
