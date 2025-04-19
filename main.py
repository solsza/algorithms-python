import ReverseList
import ZipperList


class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def main():
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
    # a -> b -> c -> d -> e -> f

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z

    ZipperList.zipper_lists(a, x)


if __name__ == '__main__':
    main()
