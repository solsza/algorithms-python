from linked_list import RemoveNode


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def main():
    # print('Hello world')
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    RemoveNode.remove_node(a, "c")

if __name__ == '__main__':
    main()