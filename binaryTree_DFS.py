class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def depthFirstValues_iterative(root):
  results = []
  stack = [root]
  
  if root is None:
    return []

  while len(stack) > 0:
      curr = stack.pop()
      results.append(curr.val)

      if curr.right != None:
          stack.append(curr.right)
      if curr.left != None:
          stack.append(curr.left)

  return results

def depthFirstValues_recursive(root):
  if root is None:
    return []

  leftResults = depthFirstValues_recursive(root.left)
  rightResults = depthFirstValues_recursive(root.right)

  return [root.val] + leftResults + rightResults

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

res1 =  depthFirstValues_iterative(a)
print(res1)
res2 = depthFirstValues_recursive(a)
print(res2)