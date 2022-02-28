class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def tree_search_BFS(root, target):
  if root is None: return False

  q = [root]

  while len(q) > 0:
    cur = q.pop(0)
    if cur.val == target: return True

    if cur.left is not None: q.append(cur.left)
    if cur.right is not None: q.append(cur.right)

  return False



a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#-------------------------------------------------------

res1 =  tree_search_BFS(a, 'F')
print(res1)
res2 = tree_search_BFS(a, 'Z')
print(res2)
