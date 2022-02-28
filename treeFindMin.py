class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def treeFindMin_DFS_iterative(root):
  minimum = float('inf')
  stack = [root]

  while len(stack):
    cur = stack.pop()
    minimum = min(minimum, cur.val)
    if cur.left is not None: stack.append(cur.left)
    if cur.right is not None: stack.append(cur.right)

  return minimum


def treeFindMin_BFS_iterative(root):
  minimum = float('inf')
  queue = [root]

  while len(queue):
    cur = queue.pop(0)
    minimum = min(minimum, cur.val)
    if cur.left is not None: queue.append(cur.left)
    if cur.right is not None: queue.append(cur.right)

  return minimum


def treeFindMin_DFS_recursive(root):
  if root is None: return float('inf')

  return min(root.val, treeFindMin_DFS_recursive(root.left), treeFindMin_DFS_recursive(root.right))


#----------------------------------

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


result = treeFindMin_BFS_iterative(a)
print(result)

result = treeFindMin_DFS_iterative(a)
print(result)

result = treeFindMin_DFS_recursive(a)
print(result)



