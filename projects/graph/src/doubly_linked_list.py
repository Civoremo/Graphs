"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # pass
    new_node = ListNode(value)
    if self.head is not None:
        old_head = self.head
        self.head = new_node
        old_head.prev = self.head
        self.head.next = old_head
        self.length += 1
    elif self.head is None:
        self.head = new_node
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length += 1
    else:
        return None

  def remove_from_head(self):
    # pass
    if self.head == self.tail:
        value = self.head.value
        self.head = None
        self.tail = None
        self.length -= 1
        return value
    elif self.head is not None:
        value = self.head.value
        new_head = self.head.next
        self.head = None
        new_head.prev = None
        self.length -= 1
        return value
    else:
        return None

  def add_to_tail(self, value):
    # pass
    new_tail = ListNode(value)
    if self.head == self.tail and self.tail is not None:
        self.tail = new_tail
        self.tail.prev = self.head
        self.head.next = self.tail
        self.length += 1
    elif self.tail is None:
        self.head = new_tail
        self.tail = new_tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length += 1
    else:
        old_tail = self.tail
        old_prev = self.tail.prev
        self.tail = new_tail
        old_tail.next = self.tail
        old_tail.prev = old_prev
        self.tail.prev = old_tail
        self.length += 1
        self.head.next = old_tail

  def remove_from_tail(self):
    # pass
    if self.tail is None:
        return None
    elif self.tail == self.head:
        value = self.tail.value
        self.tail = None
        self.head = None
        self.length -= 1
        return value
    else:
        value = self.tail.value
        new_tail = self.tail.prev
        self.tail = None
        new_tail.next = None
        self.length -= 1
        return value

  def move_to_front(self, node):
    # pass
    if self.tail == self.head and self.head is not None:
        return node
    elif self.head is None:
        self.head = node
        self.tail = self.head
        self.head.next = self.tail
        self.tail.prev = self.head
    else:
        new_tail = self.tail
        old_head = self.head
        old_head.prev = node
        self.tail = None
        self.head = node
        self.head.next = old_head

  def move_to_end(self, node):
    # pass
    if self.tail is None:
        return None
    elif self.head == self.tail and self.head is not None:
        self.tail = node
        self.head.next = self.tail
        self.tail.prev = self.head
    elif node == self.head:
        new_head = self.head.next
        old_tail = self.tail
        self.tail = self.head
        self.tail.next = None
        self.tail.prev = old_tail
        self.head = new_head
        self.head.prev = None
    elif node == self.tail:
        new_head = self.head.next
        old_tail = self.tail
        self.tail = self.head
        self.tail.next = None
        self.tail.prev = old_tail
        old_tail.next = self.tail
        self.head = new_head
    else:
        current = self.head
        while current is not node.next:
          if current == node:
            prev_node = current.prev
            next_node = current.next
            old_tail = self.tail
            self.tail = current
            self.tail.next = None
            self.tail.prev = old_tail
            old_tail.next = self.tail
            prev_node.next = next_node
            next_node.prev = prev_node
          current = current.next

  def delete(self, node):
    # pass
    if self.head == self.tail and self.head is not None:
        self.head = None
        self.tail = None
        self.length -= 1
    elif node == self.head:
        new_head = self.head.next
        self.head = new_head
        self.head.prev = None
        self.length -= 1
    elif node == self.tail:
        new_tail = self.tail.prev
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
    else:
        return None

    
  def get_max(self):
    # pass
    if self.head == self.tail:
        return self.head.value
    elif self.head is not None:
        current_node = self.head.next
        max_value = self.head
        while current_node:
            if current_node.value > max_value.value:
                max_value = current_node
            current_node = current_node.next
        return max_value.value
    else:
        return None