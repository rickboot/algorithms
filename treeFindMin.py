class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def treeFindMin_recursive(root):
  if root is None: return float('inf')

  smaller = min( treeFindMin_recursive(root.left), treeFindMin_recursive(root.right) )
  return min(smaller, root.val) 


def treeFindMin_iterative(root):
  minimum = float('-inf')
  queue = [root]

  while len(queue):
    cur = queue.pop(0)
    minimum = min(root.val, cur.val)
    if cur.left is not None: queue.append(cur.left)
    if cur.right is not None: queue.append(cur.right)

  return minimum


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(4)
f = Node(0)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


result = treeFindMin_recursive(a)
print(result)

result = treeFindMin_iterative(a)
print(result)