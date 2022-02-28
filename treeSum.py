class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# recursive DFS
def treeSum(root):
  if root is None: return 0
  return root.val + treeSum(root.left) + treeSum(root.right)


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(2)
e = Node(4)
f = Node(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


result = treeSum(a);
print(result)