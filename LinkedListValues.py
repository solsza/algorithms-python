class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_values(head):
  return linked_list_values_recursive(head, [])

def linked_list_values_recursive(head, values):
    if head is None: return values
    values.append(head.val)
    return linked_list_values_recursive(head.next, values)