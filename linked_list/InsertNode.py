class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


def insert_node(head, value, index):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head
    while current is not None:
        if count == index - 1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp

        count += 1
        current = current.next
    return head


def insert_node_recursive(head, value, index, count=0):
    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    if head is None:
        return None

    if count == index - 1:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return

    insert_node(head.next, value, index, count + 1)
    return head