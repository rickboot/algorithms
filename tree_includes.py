from logging.config import valid_ident


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes_BFS(root, target):
    queue = [root]

    while len(queue) > 0:
        cur = queue.pop(0)

        if cur.val == target:
            return True
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)

    return False


def tree_includes_DFS(root, target):
    stack = [root]

    while len(stack) > 0:
        cur = stack.pop()

        if cur.val == target:
            return True
        if cur.left is not None:
            stack.append(cur.left)
        if cur.right is not None:
            stack.append(cur.right)

    return False


def tree_includes_DFS_recurse(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    left = tree_includes_DFS_recurse(root.left, target)
    right = tree_includes_DFS_recurse(root.right, target)

    return left or right


# ----------------------
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

target = 'F'
result = tree_includes_BFS(a, target)
print(result)

target = 'F'
result = tree_includes_DFS(a, target)
print(result)

target = 'F'
result = tree_includes_DFS_recurse(a, target)
print(result)

target = 'Z'
result = tree_includes_BFS(a, target)
print(result)

target = 'Z'
result = tree_includes_DFS(a, target)
print(result)

target = 'Z'
result = tree_includes_DFS_recurse(a, target)
print(result)
