def remove_node(head, target_val):
    target_node = None
    tail_node = None
    current_node = head

    if current_node.val == target_val:
        return current_node.next

    while current_node is not None:
        if current_node.next.val == target_val:
            target_node = current_node.next
            tail_node = current_node
            break
        current_node = current_node.next

    tail_node.next = target_node.next
    return head

def remove_node_recursive(head, target_val):
  if head is None:
    return None

  if head.val == target_val:
    return head.next

  head.next = remove_node(head.next, target_val)
  return head