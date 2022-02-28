class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def treeMaxPathSum(root):
  if root is None: return float('-inf')
  if root.left is None and root.right is None: return root.val

  leftSum = treeMaxPathSum(root.left)
  rightSum = treeMaxPathSum(root.right)
  return root.val + max(leftSum, rightSum)


#------------------------------------

a = Node(-3)
b = Node(-11)
c = Node(-4)
d = Node(-2)
e = Node(-4)
f = Node(-1)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


result = treeMaxPathSum(a)
print(result)