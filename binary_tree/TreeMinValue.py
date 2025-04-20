class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  return min(root.val, smallest_left_value, smallest_right_value)


def tree_min_value_recursive(root):
  stack = [ root ]
  smallest = float("inf")
  while stack:
    current = stack.pop()
    if current.val < smallest:
      smallest = current.val

    if current.left is not None:
      stack.append(current.left)
    if current.right is not None:
      stack.append(current.right)

  return smallest